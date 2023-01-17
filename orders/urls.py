from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/<table_pk>", views.new_order, name="new_order"),
    # path("waitlist/", views.index, name="waitlist"),
]
