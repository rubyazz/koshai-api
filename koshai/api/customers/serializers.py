from api.users.serializers import UserSerializer
from customers.models import Customer
from rest_framework import serializers


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id",
            "phone",
            "full_name",
        )


class CustomerDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = (
            "id",
            "full_name",
            "phone",
            "address",
            "user",
            "avatar",
            "is_active",
        )
