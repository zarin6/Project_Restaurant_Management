from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

TABLE_SIZE = (
    (2, "2 osoby"),
    (3, "3 osoby"),
    (4, "4 osoby"),
    (5, "5 osób"),
    (6, "6 osób"),
    (7, "7 osób"),
    (8, "8 osób")
)


TIME_RESERVATION = (
    ("12:00", "12:00"),
    ("12:30", "12:30"),
    ("13:00", "13:00"),
    ("13:30", "13:30"),
    ("14:00", "14:00"),
    ("14:30", "14:30"),
    ("15:00", "15:00"),
    ("15:30", "15:30"),
    ("16:00", "16:00"),
    ("16:30", "16:30"),
    ("17:00", "17:00"),
    ("17:30", "17:30"),
    ("18:00", "18:00"),
    ("18:30", "18:30"),
    ("19:00", "19:00"),
    ("19:30", "19:30"),
    ("20:00", "20:00"),
    ("20:30", "20:30"),
    ("21:00", "21:00"),
    ("21:30", "21:30")

)


class Table(models.Model):
    table_size = models.IntegerField(choices=TABLE_SIZE)
    time_reservation = models.CharField(choices=TIME_RESERVATION, max_length=10)
    date_reservation = models.DateField()

class Accept_reservation(models.Model):
    table_size = models.IntegerField(choices=TABLE_SIZE)
    time_reservation = models.CharField(choices=TIME_RESERVATION, max_length=10)
    date_reservation = models.DateField()
