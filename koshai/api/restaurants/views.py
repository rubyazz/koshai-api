from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from restaurants.models import Restaurant

from .serializers import RestaurantDetailsSerializer, RestaurantListSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ("retrieve", "update"):
            return RestaurantDetailsSerializer
        return super().get_serializer_class()
