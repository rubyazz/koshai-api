from allauth.account.views import LoginView, SignupView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view

from .views import UserRegisterView, main

schema_view = get_swagger_view(title="Koshai API")

urlpatterns = [
    path("accounts/login/", LoginView.as_view(), name="account_login"),
    path("accounts/signup/", SignupView.as_view(), name="account_signup"),
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    path("main/", main, name="main"),
    path("", TemplateView.as_view(template_name="pages/index.html"), name="home"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("api/", include("api.routers")),
    path("docs/", schema_view),
    path("api/drf-auth/", include("rest_framework.urls")),
    path("accounts/", include("allauth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
