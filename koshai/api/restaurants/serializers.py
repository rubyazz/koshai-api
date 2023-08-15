from api.users.serializers import UserSerializer
from rest_framework import serializers
from restaurants.models import Restaurant


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
