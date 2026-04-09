from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>/", views.post_detail, name="post_detail"),
]
