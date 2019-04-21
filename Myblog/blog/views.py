from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Comment, Tag
from django.contrib.auth.decorators import login_required 
from .forms import NewBlogForm,NewCommentForm
from django.contrib.auth.models import User


class PostListView(ListView):
	model = Post
	get_recent_post_list = Post.objects.all().order_by('-create_date')[:8]
	template_name = 'home_page.html'
	paginate_by = 3

	def get_context_data(self, **kwargs):
		context = super(PostListView,self).get_context_data(**kwargs)
		context['get_recent_post_list'] = PostListView.get_recent_post_list
		return context
	

# def post_detail(request, pk):
# 	post = Post.objects.get(pk = pk)

# 	return render(request, 'post_detail.html', {'post':post})

class PostDetailView(DetailView):
	model = Post

	template_name = 'post_detail.html'

	
	


class AccountPostListView(ListView):



	

	def get_queryset(self):
		return Post.objects.filter(author = self.request.user)
	
	template_name = 'my_account.html'
	paginate_by =5
	# def get_context_data(self, **kwargs):
	# 	context = super(AccountPostListView, self).get_context_data(**kwargs)
	# 	context['account_post_list'] = self.request.user.posts.get_queryset
	# 	return context	




def other_account(request, id):
	# print(username)

	user = User.objects.get(id = id)
	post_list = user.posts.get_queryset()

	return render(request, 'other_account.html', {'ot':user, 'post_list':post_list})

@login_required		
def new_blog(request):
	if request.method =='POST':
		form = NewBlogForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('my_account')

	form = NewBlogForm()

	
	return render(request, 'new_blog.html', {'form':form})
# Create your views here.
@login_required
def add_comment(request,pk):
	if request.method =='POST':
		form = NewCommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = request.user
			comment.post = Post.objects.get(id=pk)
			comment.save()
			return redirect('post_deteil', comment.post.pk)


	form = NewCommentForm()
	post = Post.objects.get(pk=pk)
	return render(request, 'add_comment.html', {'form':form, 'post':post})