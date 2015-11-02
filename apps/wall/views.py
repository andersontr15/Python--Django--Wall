from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from apps.wall.models import User, Message, Comment
from django.contrib import messages
from django.utils import timezone
from datetime import datetime

def index(request):
	print request.GET
	print request.method
	return render(request, 'wall/index.html')

def register(request):
	print "Registration"
	user = User.objects.filter(email= request.POST.get('email'), password=request.POST.get('password'))
	if len(user) > 0 and len(request.POST.get('email'))<3:
		return redirect('/')
	else:
		user = User()
		user.first_name = request.POST.get('first_name')
		user.last_name = request.POST.get('last_name')
		user.email = request.POST.get('email')
		user.password = request.POST.get('password')
		user.save()
		print "Successful Registration"
		print user.first_name
		print user.last_name
		print user.email
		print user.password
		return redirect('/')

def login(request):
	print "Login"
	print request.POST.get('email')
	print request.POST.get('password')
	user = User.objects.filter(email=request.POST.get('email'))
	if len(user)<1:
		print "Failed"
		return redirect('/')
	else:
		print "Success"
		request.session['user_id'] = user[0].id
		print "Logging In.."
		return redirect('/dashboard')

def dashboard(request):
	print "User Dashboard"
	if "user_id" in request.session:
		user = User.objects.get(id=request.session['user_id'])
		messages = Message.objects.all().order_by('created_at').reverse()
		comments = Comment.objects.all()
		context = {
			'user': user,
			'messages': messages,
			'comments': comments
		}
		return render(request, 'wall/dashboard.html', context)
	else:
		del request.session
		return redirect('/')

def message(request):
	user = User.objects.get(id=request.session['user_id'])
	message = Message()
	message.user = user
	message.created_at = timezone.now()
	message.message = request.POST.get('message')
	message.save()
	return redirect('/dashboard')

def delete_message(request, message_id):
	message = Message.objects.get(id=message_id)
	message.delete()
	return redirect('/dashboard')

def delete_comment(request, comment_id):
	comment = Comment.objects.get(id=comment_id)
	comment.delete()
	return redirect('/dashboard')


def comment(request, message_id):
	user = User.objects.get(id=request.session['user_id'])
	message = Message.objects.get(id=message_id)
	comment = Comment()
	comment.user = user
	comment.message = message
	comment.created_at = timezone.now()
	comment.comment = request.POST.get('comment')
	comment.save()
	return redirect('/dashboard')


def logout(request):
	print "Logging Out"
	del request.session['user_id']
	return redirect('/')

