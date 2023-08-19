from django.urls import path
from rest_framework import routers

from .views import CreateOrderView, OrderHistoryView, OrderItemView

app_name = "orders"

router = routers.DefaultRouter()

urlpatterns = [
    path("orders/create-order/", CreateOrderView.as_view(), name="create-order"),
    path("orders/order-history/", OrderHistoryView.as_view(), name="order-history"),
    path("orders/order-item/", OrderItemView.as_view(), name="order-item"),
]

urlpatterns += router.urls
