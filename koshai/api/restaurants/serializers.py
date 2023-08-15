from restaurants.models import Restaurant
from rest_framework import serializers


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            "id",
            "name",
        )


class RestaurantDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            "id",
            "name",
            "address",
            "status",
        )
