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
    (8, "8 osób"),
)

class Table(models.Model):
    table_size = models.IntegerField(choices=TABLE_SIZE)
