from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "restaurant", "status", "courier", "timestamp")
    list_filter = ("status",)
    search_fields = ("customer__id", "restaurant__id")
    readonly_fields = ("timestamp",)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order_id",
        "menu_item",
        "price",
        "quantity",
    )
    search_fields = ("id",)
    readonly_fields = ("price",)
