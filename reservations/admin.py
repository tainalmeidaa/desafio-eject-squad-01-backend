from django.contrib import admin

from reservations.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer_name",
        "date",
        "start_time",
        "duration",
        "party_size",
    )
    list_display_links = ("id", "customer_name")
    list_filter = ("date", "duration", "party_size")
    search_fields = ("id", "customer_name")
    ordering = ("-date", "-start_time")
    readonly_fields = ("id",)
    fields = ("id", "customer_name", "date", "start_time", "duration", "party_size")
