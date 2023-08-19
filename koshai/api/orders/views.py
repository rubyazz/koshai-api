from api.mixins import RoleRequiredMixin
from customers.models import Customer
from orders.models import Order
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import OrderSerializer


class CreateOrderView(generics.CreateAPIView, RoleRequiredMixin):
    serializer_class = OrderSerializer
    roles_required = ["customer"] 

    def perform_create(self, serializer):
        customer = Customer.objects.get(user=self.request.user)
        serializer.save(customer=customer)


class OrderHistoryView(generics.ListAPIView, RoleRequiredMixin):
    serializer_class = OrderSerializer
    roles_required = ["customer"] 

    def get_queryset(self):
        customer = Customer.objects.get(user=self.request.user)
        return Order.objects.filter(customer=customer)
