from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from kitchen.views import update_order_status
from main_site.models import RoomTable

from .forms import OrderForm, OrderItemForm
from .models import Order, OrderItem


@login_required()
@user_passes_test(lambda u: u.is_waiter or u.is_admin)
def index(req):
    tables = RoomTable.objects.all()
    return render(req, "orders/index.html", {"tables": tables})


def waitlist(req):
    items = OrderItem.objects.filter(status__in=["2", "3", "4"]).order_by(
        "created_at"
    )
    return render(req, "orders/waitlist.html", {"items": items})


@login_required()
@user_passes_test(lambda u: u.is_waiter or u.is_admin)
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
        "orders": table.orders.filter(is_completed=False),
        "order_form": order_form,
        "item_form": item_form,
    }
    return render(req, "orders/table_orders.html", context=context)


@login_required()
@user_passes_test(lambda u: u.is_waiter or u.is_admin)
def order_item_create(req, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if req.method == "POST":
        form = OrderItemForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            price = cd["dish"].price * cd["quantity"]
            item, created = OrderItem.objects.get_or_create(
                price=price,
                dish=cd["dish"],
                order=order,
                notes=cd["notes"],
                quantity=cd["quantity"],
            )
    return redirect("table_orders_list", order.table.id)


@login_required()
@user_passes_test(lambda u: u.is_waiter or u.is_admin)
def pay_order(req, order_id):
    order = get_object_or_404(Order, pk=order_id)
    items = order.items.all()
    if order.items.count() == 0:
        return redirect("table_orders_list", order.table.id)

    print([i.status == "5" for i in items])
    if not all([i.status == "5" for i in items]):
        return redirect("table_orders_list", order.table.id)

    if req.method == "POST":
        if all([i.status == "5" for i in items]):
            order.is_completed = True
            order.save()
            return redirect("orders_index")
        else:
            return redirect("table_orders_list", order.table.id)
    else:
        return render(req, "orders/pay.html", {"order": order})


@login_required()
@user_passes_test(lambda u: u.is_waiter or u.is_admin)
def remove_order(req, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if req.method == "POST":
        items = order.items.all()
        if all([i.status == "1" for i in items]):
            order.delete()
    return redirect("table_orders_list", order.table.id)


@login_required()
@user_passes_test(lambda u: u.is_waiter or u.is_admin)
def transfer_order_to_cook(req, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.is_draft:
        order.is_draft = False
        order.save()
    if req.method == "POST":
        if order.items.count() == 0:
            redirect("table_orders_list", order.table.id)
        items = order.items.all()
        for i in items:
            if i.status == "1":
                i.status = "2"
                i.save()
    update_order_status()

    return redirect("table_orders_list", order.table.id)


@login_required()
@user_passes_test(lambda u: u.is_waiter or u.is_admin)
def deliver_item(req, item_id):
    item = get_object_or_404(OrderItem, pk=item_id)
    if item.status == "4":
        item.status = "5"
        item.save()
    return redirect("table_orders_list", item.order.table.id)


def test_json(req):
    items = (
        OrderItem.objects.filter(status__in=["2", "3", "4"])
        .order_by("created_at")
        .all()
    )
    items_dict = [
        {
            "table": i.order.table.number,
            "title": i.dish.title,
            "quantity": i.quantity,
            "status": i.get_status_display(),
            "estimated_timestamp":i.estimated_finish_time.strftime("%H:%M"),
        }
        for i in items
    ]
    return JsonResponse({"items": items_dict})
