from django import forms
from django.forms import (BaseInlineFormSet, inlineformset_factory,
                          modelformset_factory)

from .models import Order, OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["menu_item", "order", "notes", "quantity"]

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.price = obj.menu_item.price
        if commit:
            obj.save()
        return obj


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["table"]


OrderItemInlineFormSet = inlineformset_factory(
    Order, OrderItem, form=OrderItemForm
)
