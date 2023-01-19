from django.shortcuts import render

from kitchen.models import Menu


# Create your views here.
def index(req):
    menus = Menu.objects.all()
    return render(req, "main/index.html", {"menus": menus})
