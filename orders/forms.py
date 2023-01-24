from django import forms

from .models import Order, OrderItem


class OrderItemForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, initial=1, label="Количество")

    class Meta:
        model = OrderItem
        fields = ["dish", "notes", "quantity"]
        widgets = {
            "dish": forms.Select(attrs={"class": "form-control"}),
            "notes": forms.Textarea(
                attrs={"class": "form-control", "rows": "2"}
            ),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
        }
        labels = {
            "dish": "Блюдо",
            "notes": "Предпочтения",
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ["table", "is_completed", "is_draft"]
