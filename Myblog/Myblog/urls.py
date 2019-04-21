"""Myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog import views
from account import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^signup/$', account_views.signup, name = 'signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name = 'logout'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    url(r'^reset/', include('account.urls')),
    url(r'^account/$', views.AccountPostListView.as_view(), name = 'my_account'),
    url(r'^account/(?P<id>[^/])/$', views.other_account, name = 'other_account'),


    url(r'settings/password/$', auth_views.PasswordChangeView.as_view(template_name = 'password_change.html'), name = 'password_change'),
    url(r'settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(
        template_name = 'password_change_done.html'),name = 'password_change_done'),
]
