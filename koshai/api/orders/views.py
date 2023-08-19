from api.mixins import RoleRequiredMixin
from customers.models import Customer
from orders.models import Order, OrderItem
from rest_framework import generics

from .serializers import OrderItemSerializer, OrderSerializer


class CreateOrderView(RoleRequiredMixin, generics.CreateAPIView):
    serializer_class = OrderSerializer
    roles_required = ["customer"]

    def perform_create(self, serializer):
        customer = Customer.objects.get(user=self.request.user)
        serializer.save(customer=customer)


class OrderHistoryView(RoleRequiredMixin, generics.ListAPIView):
    serializer_class = OrderSerializer
    roles_required = ["customer"]

    def get_queryset(self):
        customer = Customer.objects.get(user=self.request.user)
        return Order.objects.filter(customer=customer)


class OrderItemView(RoleRequiredMixin, generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    roles_required = ["customer", "courier", "restaurant"]
