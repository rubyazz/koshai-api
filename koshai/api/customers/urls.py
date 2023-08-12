from rest_framework import routers

from .views import CustomerViewSet

app_name = "customers"

router = routers.DefaultRouter()
router.register(r"customers/customers", CustomerViewSet, basename="customers")

urlpatterns = router.urls
