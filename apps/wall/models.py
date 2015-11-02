from django.db import models

class User(models.Model):
	first_name = models.TextField(blank=False, max_length=20)
	last_name = models.TextField(blank=False, max_length=20)
	email = models.TextField(blank=False, max_length=20)
	password = models.TextField(blank=False, max_length=20)
	counter = models.IntegerField(blank=False, null=True)
	class Meta:
		db_table = 'user'

class Message(models.Model):
	user = models.ForeignKey(User, related_name="message_user")
	message = models.TextField(blank=False, max_length=200)
	created_at = models.DateField()
	class Meta:
		db_table = 'messages'


class Comment(models.Model):
	user = models.ForeignKey(User, related_name = "comment_user")
	message = models.ForeignKey(Message, related_name="comment_message", null=True)
	comment = models.TextField(blank=False, max_length=200)
	created_at = models.DateField(null=True)
	class Meta:
		db_table = 'comments'