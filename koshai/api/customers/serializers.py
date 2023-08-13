from api.users.serializers import UserSerializer
from customers.models import Customer
from rest_framework import serializers


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id",
            "full_name",
            "address",
            "is_active",
        )


class CustomerDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = (
            "id",
            "full_name",
            "address",
            "user",
            "avatar",
            "is_active",
        )
