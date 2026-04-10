import datetime

from django import forms
from django.utils import timezone

from reservations.models import (
    DURATION_CHOICES,
    Reservation,
    get_available_slots,
    get_operating_hours,
)


class ReservationForm(forms.ModelForm):
    duration = forms.TypedChoiceField(
        choices=DURATION_CHOICES,
        coerce=int,
        widget=forms.RadioSelect,
        error_messages={"invalid_choice": "Selecione uma duração válida."},
    )

    party_size = forms.IntegerField(
        min_value=1,
        max_value=6,
        error_messages={
            "min_value": "A reserva precisa ter pelo menos 1 pessoa.",
            "max_value": "Aceitamos no máximo 6 pessoas por mesa.",
        },
        widget=forms.NumberInput(attrs={"min": 1, "max": 6}),
    )

    class Meta:
        model = Reservation
        fields = ["customer_name", "date", "start_time", "duration", "party_size"]
        widgets = {
            "customer_name": forms.TextInput(attrs={"placeholder": "Seu nome"}),
            "date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["start_time"].input_formats = ["%H:%M"]

    def clean_date(self):
        date = self.cleaned_data["date"]
        if date < timezone.localdate():
            raise forms.ValidationError("Não é possível reservar em datas passadas.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        start_time = cleaned_data.get("start_time")
        duration = cleaned_data.get("duration")

        if not all([date, start_time, duration]):
            return cleaned_data

        open_time, close_time = get_operating_hours(date)

        if start_time < open_time:
            raise forms.ValidationError(
                f"O restaurante abre às {open_time:%H:%M} neste dia."
            )

        start_dt = datetime.datetime.combine(date, start_time)
        end_dt = start_dt + datetime.timedelta(minutes=duration)
        close_dt = datetime.datetime.combine(date, close_time)

        if end_dt > close_dt:
            raise forms.ValidationError(
                "A reserva ultrapassaria o horário de fechamento."
            )

        available = get_available_slots(date, duration)
        if start_time not in available:
            raise forms.ValidationError(
                "Este horário não está mais disponível. Tente outro."
            )

        return cleaned_data
