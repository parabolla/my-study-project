from django.contrib import admin
from django.urls import path

from new_app.views import index
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("new_app/", include("new_app.urls")),
    path("new_app2/", include("new_app2.urls")),
]
