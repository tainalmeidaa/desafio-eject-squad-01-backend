import datetime

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.utils.http import url_has_allowed_host_and_scheme

from reservations.forms import ReservationForm
from reservations.models import (
    VALID_DURATIONS,
    get_available_slots,
    get_operating_hours,
)


def create_reservation(request):
    if request.method != "POST":
        return redirect("website:home")

    next_url = request.POST.get("next", "")
    if not url_has_allowed_host_and_scheme(
        next_url, allowed_hosts={request.get_host()}
    ):
        next_url = reverse("website:home")

    form = ReservationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(
            request,
            "Reserva enviada com sucesso! Se precisar, você pode fazer outra reserva para grupos maiores.",
        )
    else:
        error_msgs = []
        for field_errors in form.errors.values():
            error_msgs.extend(field_errors)
        if error_msgs:
            messages.error(request, error_msgs[0])
        else:
            messages.error(
                request,
                "Não foi possível enviar a reserva. Revise os campos e tente novamente.",
            )

    return redirect(next_url)


def available_slots(request):
    date_str = request.GET.get("date", "")
    duration_str = request.GET.get("duration", "")

    try:
        target_date = datetime.date.fromisoformat(date_str)
        duration = int(duration_str)
    except (ValueError, TypeError):
        return JsonResponse({"error": "Parâmetros inválidos."}, status=400)

    if duration not in VALID_DURATIONS:
        return JsonResponse({"error": "Duração inválida."}, status=400)

    if target_date < timezone.localdate():
        return JsonResponse({"error": "Data no passado."}, status=400)

    open_time, close_time = get_operating_hours(target_date)
    slots = get_available_slots(target_date, duration)

    return JsonResponse(
        {
            "operating_hours": {
                "open": f"{open_time:%H:%M}",
                "close": f"{close_time:%H:%M}",
            },
            "available_slots": [f"{s:%H:%M}" for s in slots],
        }
    )
