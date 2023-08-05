from django.urls import path
from rest_framework import routers

from .views import whoami

router = routers.DefaultRouter()

app_name = "users"


urlpatterns = [
    path("users/whoami/", whoami, name="whoami"),
]

urlpatterns += router.urls
