from api.mixins import RoleRequiredMixin
from rest_framework.viewsets import ModelViewSet
from restaurants.models import CategoryMenuItem, MenuItem, Restaurant

from .serializers import (
    CategoryMenuItemSerializer,
    MenuItemSerializer,
    RestaurantDetailsSerializer,
    RestaurantListSerializer,
)


class RestaurantViewSet(RoleRequiredMixin, ModelViewSet):
    """Restaurant CRUD api"""

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    roles_required = ["restaurant"]

    def get_serializer_class(self):
        if self.action in ("retrieve", "update"):
            return RestaurantDetailsSerializer
        return super().get_serializer_class()


class CategoryMenuItemViewSet(RoleRequiredMixin, ModelViewSet):
    """Category of MenuItem CRUD api"""

    queryset = CategoryMenuItem.objects.all()
    serializer_class = CategoryMenuItemSerializer
    roles_required = ["customer", "restaurant"]


class MenuItemViewSet(RoleRequiredMixin, ModelViewSet):
    """MenuItem CRUD api"""

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    roles_required = ["customer", "restaurant"]
