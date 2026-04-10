from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, "blog/blog.html")

def article(request):
    return render(request, "blog/article/article-detail.html")