from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index),
]


"""
class Menu(models.Model):
    pass


class MenuItem():
    pass


class Order(models.Model):
    pass

class OrderItem(models.Model):
    pass

"""
