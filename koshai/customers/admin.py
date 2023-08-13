from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "address",
        "user",
        "avatar",
        "is_active",
    )
    list_filter = (
        "full_name",
        "is_active",
    )
    search_fields = ("user__username",)
