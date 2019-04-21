from django.conf.urls import url
from django.contrib.auth import views

urlpatterns =[
	url(r'^$', views.PasswordResetView.as_view(
		template_name = 'password_reset.html', 
		email_template_name = 'passowrd_reset_email.html',
		subject_template_name = 'password_reset_subject.txt'),
	name = 'password_reset'),
	url(r'^done/$',
		views.PasswordResetDoneView.as_view(
			template_name = 'password_reset_done.html'),
		name = 'password_reset_done'),
	url(r'(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		views.PasswordResetConfirmView.as_view(
			template_name = 'password_reset_confirm.html'),
		name = 'password_reset_confirm'),
	url(r'complete/$', 
		views.PasswordResetCompleteView.as_view(
			template_name = 'password_reset_complete.html'),
		name = 'password_reset_complete'),

	
]