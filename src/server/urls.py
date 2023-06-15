"""
URL configuration for financial_transactions project.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("server.apps.api.urls")),
]
