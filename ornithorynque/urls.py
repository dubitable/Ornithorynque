from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("basketballtrainer/", include("basketballtrainer.urls")),
    path("admin/", admin.site.urls),
]
