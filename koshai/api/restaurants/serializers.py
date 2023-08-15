from restaurants.models import Restaurant
from rest_framework import serializers
from api.users.serializers import UserSerializer

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
