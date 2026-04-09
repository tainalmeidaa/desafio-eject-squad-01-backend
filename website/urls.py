from django.urls import path

from website import views

app_name = "app"

urlpatterns = [
    path("", views.home, name="home"),
]
