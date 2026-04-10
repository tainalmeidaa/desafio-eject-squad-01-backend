from reservations.forms import ReservationForm


def reservation_form(request):
    return {"reservation_form": ReservationForm()}
