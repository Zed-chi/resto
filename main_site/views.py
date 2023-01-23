from django.shortcuts import render

from kitchen.models import Menu


def index(req):
    menus = Menu.objects.all()
    return render(req, "main/index.html", {"menus": menus})
