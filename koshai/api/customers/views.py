from customers.models import Customer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import CustomerDetailsSerializer, CustomerListSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ("retrieve", "update"):
            return CustomerDetailsSerializer
        return super().get_serializer_class()
