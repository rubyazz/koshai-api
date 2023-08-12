from django.urls import path, include
from rest_framework import routers

from .views import CreateOrderView, OrderHistoryView

app_name = "orders"

router = routers.DefaultRouter()

urlpatterns = [
    path("orders/create-order/", CreateOrderView.as_view(), name="create-order"),
    path("orders/order-history/", OrderHistoryView.as_view(), name="order-history"),
]

urlpatterns += router.urls
