from django.db import models

from kitchen.models import Dish
from main_site.models import RoomTable


class Order(models.Model):
    table = models.ForeignKey(
        RoomTable, on_delete=models.CASCADE, related_name="orders"
    )
    is_completed = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=True)

    def price(self):
        return sum(map(lambda x: x.price * x.quantity, self.items))


class OrderItem(models.Model):
    STATUSES = [
        (
            "1",
            "Черновик",
        ),
        (
            "2",
            "В ожидании",
        ),
        (
            "3",
            "Готовится",
        ),
        (
            "4",
            "Готово",
        ),
        ("5", "Доставлено"),
    ]
    price = models.DecimalField(decimal_places=2, max_digits=10)
    dish = models.ForeignKey(
        Dish, on_delete=models.CASCADE, related_name="order_items"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items"
    )
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUSES, max_length=50, default="1")
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    started_to_cook = models.DateTimeField(
        auto_now_add=False, null=True, blank=True
    )
