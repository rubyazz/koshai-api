from orders.models import Order, OrderItem
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "customer",
            "restaurant",
            "status",
            "courier",
            "timestamp",
        )


class OrderItemSerializer(serializers.ModelSerializer):
    order_id = OrderSerializer()

    class Meta:
        model = OrderItem
        fields = ("id", "order_id", "menu_item", "price", "quantity")
