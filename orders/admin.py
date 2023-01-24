from django.contrib import admin

from .models import Order, OrderItem


admin.site.register(OrderItem)



class OrderItemInline(admin.StackedInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline,]