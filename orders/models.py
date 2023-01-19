from django.db import models

from main_site.models import MenuItem, RoomTable


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
            "draft",
        ),
        (
            "2",
            "waiting",
        ),
        (
            "3",
            "cooking",
        ),
        (
            "4",
            "finished",
        ),
        ("5", "delivered"),
    ]
    price = models.DecimalField(decimal_places=2, max_digits=10)
    menu_item = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE, related_name="order_items"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items"
    )
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUSES, max_length=50, default="1")
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
