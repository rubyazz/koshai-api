from api.mixins import RoleRequiredMixin
from couriers.models import Courier
from rest_framework.viewsets import ModelViewSet

from .serializers import CourierDetailsSerializer, CourierListSerializer


class CourierViewSet(RoleRequiredMixin, ModelViewSet):
    """Couriers CRUD api"""

    queryset = Courier.objects.all()
    serializer_class = CourierListSerializer
    roles_required = ["courier"]

    def get_serializer_class(self):
        if self.action in ("retrieve", "update"):
            return CourierDetailsSerializer
        return super().get_serializer_class()
