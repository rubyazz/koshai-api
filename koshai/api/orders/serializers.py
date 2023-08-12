from orders.models import Order
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
