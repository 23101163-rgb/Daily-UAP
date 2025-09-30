from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'news/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/post_detail.html', {'post': post})
