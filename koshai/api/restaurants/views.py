from rest_framework.viewsets import ModelViewSet
from api.mixins import RoleRequiredMixin
from restaurants.models import Restaurant, MenuItem, CategoryMenuItem
from .serializers import RestaurantDetailsSerializer, RestaurantListSerializer, CategoryMenuItemSerializer, MenuItemSerializer

class RestaurantViewSet(RoleRequiredMixin, ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    roles_required = ["restaurant"]  

    def get_serializer_class(self):
        if self.action in ("retrieve", "update"):
            return RestaurantDetailsSerializer
        return super().get_serializer_class()

class CategoryMenuItemViewSet(RoleRequiredMixin, ModelViewSet):
    queryset = CategoryMenuItem.objects.all()
    serializer_class = CategoryMenuItemSerializer
    roles_required = ["customer", "restaurant"] 

class MenuItemViewSet(RoleRequiredMixin, ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    roles_required = ["customer", "restaurant"] 
