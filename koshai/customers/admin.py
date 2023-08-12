from django.contrib import admin
from .models import Customer
from orders.models import Order

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0
    readonly_fields = ["id", "status"]  

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "email", "address", "user", "avatar", "is_active")
    list_filter = ("is_active",)
    search_fields = ("phone", "email", "user__username")
    readonly_fields = ("user",)
    inlines = [OrderInline]  
