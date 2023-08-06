from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Courier

@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "status", "coordinates")
    list_filter = ("status",)
    search_fields = ("phone",)
    fieldsets = (
        (
            None,
            {
                "fields": ("phone", "status", "coordinates"),
            },
        ),
    )
