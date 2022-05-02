from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	template_name = 'blog_list.html'

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'blog_post.html'
