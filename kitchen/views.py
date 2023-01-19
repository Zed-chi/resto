from django.shortcuts import get_object_or_404, redirect, render

from orders.models import OrderItem

from .models import Recipe


# Create your views here.
def order_items_list(req):
    items = OrderItem.objects.filter(order__is_completed=False)
    return render(req, "cook/orderlist.html", {"items": items})


def recipe_detail(req, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(req, "cook/recipe.html", {"recipe": recipe})


def order_item_cooked(request, pk):
    item = get_object_or_404(OrderItem, pk=pk)
    item.status = "4"
    item.save()
    return redirect("order_items_list")
