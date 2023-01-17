from django.forms import inlineformset_factory
from django.shortcuts import redirect, render

from main_site.models import RoomTable

from .forms import OrderForm, OrderItemForm
from .models import Order, OrderItem


def index(req):
    tables = RoomTable.objects.all()
    return render(req, "orders.html", {"tables": tables})


def new_order(req, table_pk):
    table = RoomTable.objects.get(pk=table_pk)
    Order_item_fset = inlineformset_factory(
        Order, OrderItem, form=OrderItemForm, extra=1
    )

    order, created = Order.objects.get_or_create(
        table=table, is_completed=False
    )
    if req.method == "POST":
        print(req.POST)
        formset = Order_item_fset(req.POST, instance=order)

        if formset.is_valid():
            formset.save()
            return redirect("index")
        else:
            formset.save()
            print(formset.errors)
    else:
        formset = Order_item_fset(instance=order)
        print(dir(formset))
    context = {"formset": formset, "order": order}
    return render(req, "new_order.html", context=context)
