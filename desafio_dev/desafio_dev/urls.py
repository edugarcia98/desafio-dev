from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cnab/", include(("cnab.routes", "cnab"), namespace="cnab")),
]
