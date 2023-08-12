from django.contrib import admin
from orders.models import Order

from .models import Customer


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0
    readonly_fields = ["id", "status"]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "address", "user", "avatar", "is_active")
    list_filter = ("is_active",)
    search_fields = ("phone", "user__username")
    inlines = [OrderInline]
