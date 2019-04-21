from django.db import models
from django.contrib.auth.models import User
from markdown import markdown
from django.utils.html import mark_safe

class Tag(models.Model):
	tag = models.CharField(max_length = 30, null = True, blank =True)

	def __str__(self):
		return self.tag



class Post(models.Model):
	title = models.CharField(max_length = 30)
	text = models.TextField(max_length = 4000)
	author = models.ForeignKey(User, related_name = 'posts')
	create_date = models.DateTimeField(auto_now_add = True)
	updata_date = models.DateTimeField(auto_now_add = True)
	tags = models.ManyToManyField(Tag, related_name = 'posts', blank = True)
	views = models.PositiveIntegerField(default = 0)

	def __str__(self):
		return self.title
	def get_comments_counts(self):
		 return Comment.objects.filter(post =self).count()

	def get_comments_list(self):
		return Comment.objects.filter(post=self).order_by('-create_date')

	def get_text_as_markdown(self):
		return mark_safe(markdown(self.text, safe_mode = 'escape'))

	
class Comment(models.Model):
	comment = models.CharField(max_length = 600, null = True)
	author = models.ForeignKey(User, related_name = 'comments')
	create_date = models.DateTimeField(auto_now_add = True)
	post = models.ForeignKey(Post, related_name = 'comments')

	def __str__(self):
		return self.comment
# Create your models here.
