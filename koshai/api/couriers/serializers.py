from couriers.models import Courier
from rest_framework import serializers
from api.users.serializers import UserSerializer

class CourierListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Courier
        fields = (
            "id",
            "first_name",
            "last_name",
            "user",
            "phone",
            "status",
            "coordinates",
        )


class CourierDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Courier
        fields = (
            "id",
            "first_name",
            "last_name",
            "user",
            "phone",
            "status",
            "coordinates",
        )
