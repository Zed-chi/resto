from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import LoginForm


def index(req):
    return redirect("login")


def login(req):
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                req,
                username=cd["email"],
                password=cd["password"],
            )
            print(user)
            if user:
                if user.is_active:
                    login(req, user)
                    return redirect("main")
                else:
                    return HttpResponse("Disabled Account")
        else:
            print(form.errors)
            print(form.cleaned_data)
            return HttpResponse("Invalid User")
    else:
        form = LoginForm()
    return render(req, "users/login.html", {"form": form})


def profile_detail(req):
    return render(req, "users/profile.html")
