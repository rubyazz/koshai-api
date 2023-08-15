from rest_framework import routers

from .views import CourierViewSet

app_name = "restaurants"

router = routers.DefaultRouter()
router.register(r"couriers/couriers", CourierViewSet, basename="couriers")

urlpatterns = router.urls

