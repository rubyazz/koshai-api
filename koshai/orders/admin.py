from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "restaurant", "status", "courier", "timestamp")
    list_filter = ("status",)
    search_fields = ("customer__id", "restaurant__id")
    readonly_fields = ("timestamp",)
