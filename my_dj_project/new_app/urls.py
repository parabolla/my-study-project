from django.urls import path

from .views import *

urlpatterns = [
    path("", index),
    path("caption/", caption),
    path("blog/", blog),
]