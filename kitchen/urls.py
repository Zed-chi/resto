from django.urls import path

from . import views

urlpatterns = [
    path("", views.order_items_list, name="order_items_list"),
    path("recipe/<int:pk>", views.recipe_detail, name="recipe_detail"),
    path(
        "items/<int:pk>/got_cooked/",
        views.order_item_cooked,
        name="item_finished",
    ),
]
