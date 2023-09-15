import django_filters.rest_framework as filters
from api.mixins import RoleRequiredMixin
from customers.models import Customer
from django.views.decorators.cache import cache_page
from orders.models import Order, OrderItem
from rest_framework import generics

from .filters import OrderFilter
from .serializers import OrderItemSerializer, OrderSerializer


class CreateOrderView(RoleRequiredMixin, generics.CreateAPIView):
    serializer_class = OrderSerializer
    roles_required = ["customer"]

    @cache_page(60 * 15)
    def perform_create(self, serializer):
        customer = Customer.objects.get(user=self.request.user)
        serializer.save(customer=customer)


class OrderHistoryView(RoleRequiredMixin, generics.ListAPIView):
    serializer_class = OrderSerializer
    roles_required = ["customer"]
    filterset_class = OrderFilter
    filter_backends = [filters.DjangoFilterBackend]

    def get_queryset(self):
        customer = Customer.objects.get(user=self.request.user)
        return Order.objects.filter(customer=customer)


class OrderItemView(RoleRequiredMixin, generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    roles_required = ["customer", "courier", "restaurant"]
