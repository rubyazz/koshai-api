from orders.models import Order
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import OrderSerializer


class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderHistoryView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(customer=user.customer)
