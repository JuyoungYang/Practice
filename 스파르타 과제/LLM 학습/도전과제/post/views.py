# post/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, "post/post_list.html", {"posts": posts})


def post_write(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post:detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "post/post_form.html", {"form": form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post/post_detail.html", {"post": post})
