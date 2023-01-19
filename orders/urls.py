from django.urls import path

from . import views

urlpatterns = [
    path("waitlist/", views.waitlist, name="waitlist"),
    path(
        "table/<table_id>", views.table_orders_list, name="table_orders_list"
    ),
    path("<order_id>/pay", views.pay_order, name="pay_order"),
    path("<order_id>/remove", views.remove_order, name="remove_order"),
    path(
        "<order_id>/cook",
        views.transfer_order_to_cook,
        name="transfer_order_to_cook",
    ),
    path("<order_id>", views.order_item_create, name="order_item_create"),
    path("", views.index, name="index"),
]
