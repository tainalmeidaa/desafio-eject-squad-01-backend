from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("about_us/", views.about_us, name="about_us"),
    path("blog/", views.blog, name="blog"),
]
