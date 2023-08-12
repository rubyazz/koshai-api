from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("", include("api.users.urls", namespace="users")),
    # path("", include("api.couriers.urls", namespace="couriers")),
    # path("", include("api.customers.urls", namespace="customers")),
    path("", include("api.orders.urls", namespace="orders")),
    # path("", include("api.restaurants.urls", namespace="users")),
]
