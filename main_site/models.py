from django.db import models

from kitchen.models import Dish


class Room(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class RoomTable(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="tables"
    )
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.room.title} - {self.number}"
