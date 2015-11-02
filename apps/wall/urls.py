from django.conf.urls import patterns, url
from apps.wall import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'register$', views.register, name="register"),
	url(r'login$', views.login, name="login"),
	url(r'dashboard$', views.dashboard, name="dashboard"),
	url(r'logout$', views.logout, name="logout"),
	url(r'message$', views.message, name="message"),
	url(r'^comment/(?P<message_id>\d+)/$', views.comment, name="comment"),
	url(r'^message/(?P<message_id>\d+)/delete$', views.delete_message, name="delete_message"),
	url(r'comment/(?P<comment_id>\d+)/delete$', views.delete_comment, name="delete_comment"),

)