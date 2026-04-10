import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

TOTAL_TABLES = 28

DURATION_CHOICES = [
    (30, "30 min"),
    (60, "1 h"),
    (90, "1 h 30 min"),
    (120, "2 h"),
    (150, "2 h 30 min"),
]

VALID_DURATIONS = {c[0] for c in DURATION_CHOICES}


def get_operating_hours(target_date):
    if target_date.weekday() >= 5:
        return datetime.time(12, 0), datetime.time(22, 0)
    return datetime.time(13, 0), datetime.time(22, 0)


def get_available_slots(target_date, duration_minutes):
    open_time, close_time = get_operating_hours(target_date)

    open_dt = datetime.datetime.combine(target_date, open_time)
    close_dt = datetime.datetime.combine(target_date, close_time)
    duration_td = datetime.timedelta(minutes=duration_minutes)

    slots = []
    current = open_dt
    while current + duration_td <= close_dt:
        slots.append(current.time())
        current += duration_td

    now = timezone.localtime()
    if target_date == now.date():
        slots = [s for s in slots if s > now.time()]

    reservations = Reservation.objects.filter(date=target_date)
    ranges = []
    for r in reservations:
        r_start = datetime.datetime.combine(target_date, r.start_time)
        r_end = r_start + datetime.timedelta(minutes=r.duration)
        ranges.append((r_start, r_end))

    available = []
    for slot_time in slots:
        slot_start = datetime.datetime.combine(target_date, slot_time)
        slot_end = slot_start + duration_td
        overlapping = sum(
            1 for r_start, r_end in ranges if r_start < slot_end and r_end > slot_start
        )
        if overlapping < TOTAL_TABLES:
            available.append(slot_time)

    return available


class Reservation(models.Model):
    customer_name = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.PositiveSmallIntegerField(choices=DURATION_CHOICES)
    party_size = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)]
    )

    @property
    def end_time(self):
        start_dt = datetime.datetime.combine(self.date, self.start_time)
        end_dt = start_dt + datetime.timedelta(minutes=self.duration)
        return end_dt.time()

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-date", "-start_time"]

    def __str__(self):
        return f"{self.customer_name} - {self.date} {self.start_time:%H:%M}"
