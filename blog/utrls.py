from django.urls import path

from home import views

app_name = "blog"

urlpatterns = [
    path("", views.blog, name="home"),
]
