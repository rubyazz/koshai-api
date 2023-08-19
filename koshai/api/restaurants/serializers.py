from api.users.serializers import UserSerializer
from rest_framework import serializers
from restaurants.models import CategoryMenuItem, MenuItem, Restaurant


class RestaurantListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Restaurant
        fields = (
            "id",
            "name",
            "user",
            "address",
            "status",
        )


class RestaurantDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Restaurant
        fields = (
            "id",
            "name",
            "user",
            "address",
            "status",
        )


class CategoryMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMenuItem
        fields = ("id", "name", "is_active")


class MenuItemSerializer(serializers.ModelSerializer):
    category = CategoryMenuItemSerializer()

    class Meta:
        model = MenuItem
        fields = ("id", "name", "price", "image", "category", "description")
