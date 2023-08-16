from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
from django.views.generic import TemplateView


from . import views

schema_view = get_swagger_view(title="Koshai API")

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path("admin/", admin.site.urls),
    path("main", views.main, name="main"),
    path("", TemplateView.as_view(template_name="pages/index.html"), name="home"),

    path("api/", include("api.routers")),
    path("docs/", schema_view),
    path("api/drf-auth/", include("rest_framework.urls")),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
