from django.urls import include, path
from rest_framework import routers

app_name = "api"

urlpatterns = [
    path("", include("api.users.urls", namespace="users")),
]
