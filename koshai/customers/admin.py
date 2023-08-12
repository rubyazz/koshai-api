from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "email", "address", "user", "avatar", "is_active")
    list_filter = ("is_active",)
    search_fields = ("phone", "email", "user__username")
    readonly_fields = ("user",)
