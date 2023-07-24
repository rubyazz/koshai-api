from django.urls import include, path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView


app_name = "api"

urlpatterns = [
    path("", include("koshai.api.users.urls", namespace="users")),

    # path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("token/v2/", ObtainTokenView.as_view(), name="token_obtain"),
    # path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]