from django.urls import path
from post.views import *

from .views import *

urlpatterns = [
    path("", index),
]