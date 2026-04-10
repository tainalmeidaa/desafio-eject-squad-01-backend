from django.urls import path

from reservations import views

app_name = "reservations"

urlpatterns = [
    path("create/", views.create_reservation, name="create_reservation"),
    path("available-slots/", views.available_slots, name="available_slots"),
]
