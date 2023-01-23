from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from orders.models import OrderItem

from .models import Recipe


@login_required()
@user_passes_test(lambda u: u.is_cook or u.is_admin)
def order_items_list(req):
    finished_items = OrderItem.objects.filter(status="4")
    cooking_items = OrderItem.objects.filter(status="3")
    waiting_items = OrderItem.objects.filter(status="2").order_by("created_at")
    return render(
        req,
        "cook/orderlist.html",
        {
            "finished_items": finished_items,
            "cooking_items": cooking_items,
            "waiting_items": waiting_items,
        },
    )


@login_required()
def recipe_detail(req, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(req, "cook/recipe.html", {"recipe": recipe})


@login_required()
@user_passes_test(lambda u: u.is_cook or u.is_admin)
def order_item_cooked(request, pk):
    item = get_object_or_404(OrderItem, pk=pk)
    item.status = "4"
    item.save()
    update_order_status()
    return redirect("order_items_list")


def update_order_status():
    cooking_items = OrderItem.objects.filter(status="3")
    if cooking_items.count() == 0:
        waiting_items = OrderItem.objects.filter(status="2").order_by(
            "created_at"
        )
        if waiting_items:
            item = waiting_items[0]
            item.status = "3"
            item.save()


def get_short(qs):
    return [
        {
            "title": i.dish.title,
            "quantity": i.quantity,
        }
        for i in qs
    ]


def get_full(qs):
    return [
        {
            "title": i.dish.title,
            "notes": i.notes,
            "quantity": i.quantity,
            "status": i.get_status_display(),
            "recipe_id": i.recipe.id if hasattr(i, "recipe") else "",
            "id": i.id,
        }
        for i in qs
    ]


@login_required()
def test_json(req):
    finished_items = OrderItem.objects.filter(status="4").all()
    cooking_items = OrderItem.objects.filter(status="3").all()
    waiting_items = (
        OrderItem.objects.filter(status="2").order_by("created_at").all()
    )

    return JsonResponse(
        {
            "finished": get_short(finished_items),
            "cooking": get_full(cooking_items),
            "waiting": get_full(waiting_items),
        }
    )
