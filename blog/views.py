from django.shortcuts import get_object_or_404, render
from markdownx.utils import markdownify

from blog.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    html_content = markdownify(post.content)
    return render(
        request,
        "blog/post-detail.html",
        {"post": post, "html_content": html_content},
    )
