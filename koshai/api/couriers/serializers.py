from couriers.models import Courier
from rest_framework import serializers


class CourierListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone",
            "status",
            "coordinates",
        )


class CourierDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone",
            "status",
            "coordinates",
        )
