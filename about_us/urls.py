from django.urls import path

from about_us import views

app_name = "about_us"

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>/", views.post_detail, name="post_detail"),
]
