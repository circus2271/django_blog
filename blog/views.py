#from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import ListView

#post = Post.objects.exlude(author='rodionoff')

class PostList(ListView):
    model = Post
    context_object_name = 'post_list'
