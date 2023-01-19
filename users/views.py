from django.shortcuts import redirect, render


def index(req):
    return redirect("login")


def profile_detail(req):
    return render(req, "users/profile.html")
