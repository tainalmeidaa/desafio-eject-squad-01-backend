from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("about_us/", views.about_us, name="about_us"),
    path("blog/", views.blog, name="blog"),
    path("blog/article_detail/", views.article, name="article_detail"),
]
