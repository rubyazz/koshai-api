from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "status")
    list_filter = ("status",)
    search_fields = ("name", "address")
