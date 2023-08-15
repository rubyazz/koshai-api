from rest_framework import routers

from .views import RestaurantViewSet

app_name = "restaurants"

router = routers.DefaultRouter()
router.register(r"restaurants/restaurants", RestaurantViewSet, basename="restaurants")

urlpatterns = router.urls
