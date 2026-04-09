from django.shortcuts import get_object_or_404, render

from blog.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "blog/post-detail.html", {"post": post})
