from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from couriers.models import Courier

from .serializers import CourierDetailsSerializer, CourierListSerializer


class CourierViewSet(ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierListSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ("retrieve", "update"):
            return CourierDetailsSerializer
        return super().get_serializer_class()
