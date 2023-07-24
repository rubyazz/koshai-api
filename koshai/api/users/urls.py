from django.urls import path
from rest_framework import routers

# from .views import change_password, whoami
from .views import whoami

router = routers.DefaultRouter()

app_name = "users"


urlpatterns = [
    path("users/whoami/", whoami, name="whoami"),
    # path("users/whoami/", whoami, name="whoami"),
    # path("users/change-password/", change_password, name="change_password"),
]

urlpatterns += router.urls