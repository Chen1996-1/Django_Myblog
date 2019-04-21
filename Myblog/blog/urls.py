from django.conf.urls import url
from .views import PostListView, PostDetailView, new_blog, add_comment

urlpatterns = [
	url(r'^$', PostListView.as_view(), name = 'home_page'),
	url(r'^(?P<pk>[\d+])/$',PostDetailView.as_view() , name = 'post_deteil'),
	url(r'^new/$', new_blog, name = 'new_blog'),
	url(r'^(?P<pk>[\d+])/comment/$', add_comment, name = 'add_comment'),

]