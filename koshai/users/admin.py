from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "role",
        "is_active",
    )

    search_fields = ("first_name", "last_name", "email")

    fieldsets = (
        ("Login", {"fields": ("email", "phone_number", "password", "role")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
