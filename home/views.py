from django.shortcuts import render


def home(request):
    return render(request, "website/home.html")


def about_us(request):
    return render(request, "website/about-us.html")


def blog(request):
    return render(request, "website/blog.html")
