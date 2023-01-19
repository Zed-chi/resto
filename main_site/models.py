from django.db import models

from cookery.models import Dish


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


class Menu(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class MenuCategory(models.Model):
    title = models.CharField(max_length=255)
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name="categories"
    )

    def __str__(self):
        return f"{self.menu.title} - {self.title}"


class MenuItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    category = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE, related_name="items"
    )
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.category.title} - {self.dish.title}"

    def title(self):
        return self.dish.title
