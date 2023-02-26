from django.urls import path

from .views import *


urlpatterns = [
    path("", index2),
    path("caption/", caption2),
    path("blog/", blog2),
]