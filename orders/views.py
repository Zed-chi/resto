from django.shortcuts import get_object_or_404, redirect, render

from main_site.models import RoomTable

from .forms import OrderForm, OrderItemForm
from .models import Order, OrderItem


def index(req):
    tables = RoomTable.objects.all()
    return render(req, "orders/index.html", {"tables": tables})


def waitlist(req):
    orders = Order.objects.filter(is_completed=False, is_draft=False)
    return render(req, "orders/waitlist.html", {"orders": orders})


def table_orders_list(req, table_id):
    table = RoomTable.objects.get(pk=table_id)
    if req.method == "POST":
        Order.objects.create(table=table)
        return redirect("table_orders_list", table_id)
    else:
        order_form = OrderForm()
        item_form = OrderItemForm()
    context = {
        "table": table,
        "order_form": order_form,
        "item_form": item_form,
    }
    return render(req, "orders/table_orders.html", context=context)


def order_item_create(req, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if req.method == "POST":
        form = OrderItemForm(req.POST)
        if form.is_valid():
            if order.is_draft:
                order.is_draft = False
                order.save()
            cd = form.cleaned_data
            price = cd["menu_item"].price * cd["quantity"]
            item, created = OrderItem.objects.get_or_create(
                price=price,
                menu_item=cd["menu_item"],
                order=order,
                notes=cd["notes"],
                quantity=cd["quantity"],
            )
    return redirect("table_orders_list", order.table.id)


def pay_order(req, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if req.method == "POST":
        form = OrderItemForm(req.POST)
        if form.is_valid():
            if order.is_draft:
                order.is_draft = False
                order.save()
            cd = form.cleaned_data
            price = cd["menu_item"].price * cd["quantity"]
            item, created = OrderItem.objects.get_or_create(
                price=price,
                menu_item=cd["menu_item"],
                order=order,
                notes=cd["notes"],
                quantity=cd["quantity"],
            )
    return redirect("table_orders_list", order.table.id)


def remove_order(req, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if req.method == "POST":
        items = order.items.all()
        if all([i.status == "1" for i in items]):
            order.delete()
    return redirect("table_orders_list", order.table.id)


def transfer_order_to_cook(req, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if req.method == "POST":
        items = order.items.all()
        for i in items:
            if i.status == "1":
                i.status = "2"
                i.save()

    return redirect("table_orders_list", order.table.id)
