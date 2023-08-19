from rest_framework import routers

from .views import RestaurantViewSet, CategoryMenuItemViewSet, MenuItemViewSet

app_name = "restaurants"

router = routers.DefaultRouter()
router.register(r"restaurants/restaurants", RestaurantViewSet, basename="restaurants")
router.register(r"restaurants/categories", CategoryMenuItemViewSet, basename="category")
router.register(r"restaurants/items", MenuItemViewSet, basename="menu-item")

urlpatterns = router.urls
