from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post
# Create your views here.

def post_list(request):
    all_posts = Post.published.all()

    return render(request, 'blog/post/post_list.html',{'all_posts':all_posts})


def post_detail(request,id):
    post = get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)
    return render(request,'blog/post/post_detail.html',{'post':post})
