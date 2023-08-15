from api.restauth.views import ObtainTokenView
from django.urls import include, path
from rest_framework_simplejwt.views import TokenVerifyView

app_name = "api"

urlpatterns = [
    path("", include("api.users.urls", namespace="users")),
    path("", include("api.couriers.urls", namespace="couriers")),
    path("", include("api.customers.urls", namespace="customers")),
    path("", include("api.orders.urls", namespace="orders")),
    path("", include("api.restaurants.urls", namespace="restaurants")),
    path("token/", ObtainTokenView.as_view(), name="token_obtain"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
