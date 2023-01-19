from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="main"),
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
