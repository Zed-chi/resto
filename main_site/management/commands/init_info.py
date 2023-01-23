from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from django.db import models

from kitchen.models import Dish, Menu, MenuCategory
from main_site.models import Room, RoomTable


class Command(BaseCommand):
    help = "Creates initial model instances"

    def handle(self, *args, **kwargs):

        room = Room.objects.create(title="Главное помещение")
        for i in range(1, 5):
            RoomTable.objects.create(room=room, number=i)

        menu = Menu.objects.create(title="Главное")
        salad = MenuCategory.objects.create(title="Салаты", menu=menu)
        Dish.objects.create(title="Крабовый", category=salad, price=100)
        Dish.objects.create(title="Цезарь", category=salad, price=150)
        Dish.objects.create(title="Рыбный", category=salad, price=130)

        soup = MenuCategory.objects.create(title="Супы", menu=menu)
        Dish.objects.create(title="Рыбный", category=soup, price=100)
        Dish.objects.create(title="Сырный", category=soup, price=150)
        Dish.objects.create(title="Грибной", category=soup, price=160)

        drink = MenuCategory.objects.create(title="Напитки", menu=menu)
        Dish.objects.create(title="Чай", category=drink, price=100)
        Dish.objects.create(title="пиво", category=drink, price=100)
        Dish.objects.create(title="Квас", category=drink, price=100)

        print("initial models created")
