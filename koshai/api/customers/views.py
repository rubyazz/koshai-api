from api.mixins import RoleRequiredMixin
from customers.models import Customer
from rest_framework.viewsets import ModelViewSet

from .serializers import CustomerDetailsSerializer, CustomerListSerializer


class CustomerViewSet(RoleRequiredMixin, ModelViewSet):
    """CRUD api of customers"""

    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer
    roles_required = ["customer"]

    def get_serializer_class(self):
        if self.action in ("retrieve", "update"):
            return CustomerDetailsSerializer
        return super().get_serializer_class()
