from django.contrib import admin

from .models import CategoryMenuItem, MenuItem, Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user", "address", "status")
    list_filter = ("status",)
    search_fields = ("name", "address")


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "restaurant",
        "price",
        "image",
        "category",
        "description",
    )
    list_filter = ("price",)
    search_fields = ("name", "restaurant")


@admin.register(CategoryMenuItem)
class CategoryMenuItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "restaurant",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("name",)
