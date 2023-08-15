from django.contrib import admin

from .models import Courier


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "user",
        "status",
        "coordinates",
    )
    list_filter = ("status",)
    search_fields = (
        "first_name",
        "last_name",
    )
    fieldsets = (
        (
            None,
            {
                "fields": ("first_name", "last_name", "user", "status", "coordinates"),
            },
        ),
    )
