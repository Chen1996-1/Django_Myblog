from django import forms
from .models import Post, Comment




# title = models.CharField(max_length = 30)
# text = models.TextField(max_length = 4000)
# author = models.ForeignKey(User, related_name = 'posts')
# create_date = models.DateTimeField(auto_now_add = True)
# updata_date = models.DateTimeField(auto_now_add = True)
# tags = models.ManyToManyField(Tag, related_name = 'posts', blank = True)
# views = models.PositiveIntegerField(default = 0)

class NewBlogForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title','text']

# comment = models.CharField(max_length = 600, null = True)
# author = models.ForeignKey(User, related_name = 'comments')
# create_date = models.DateTimeField(auto_now_add = True)
# post = models.ForeignKey(Post, related_name = 'comments')

class NewCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']
