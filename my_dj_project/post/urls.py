from django.urls import path
from new_app.views import *



urlpatterns = [
    path("", index),
    # path("all_posts/", all_posts, name="all_posts"),
    path("post_detail/<int:post_id>/", post_detail, name="detail"),
    path("post_create/", post_create, name="create"),
    path("post_update/<int:post_id>/", post_update, name="update"),
    path("post_delete/<int:post_id>/", post_delete, name="delete"),
    path("favorites/", favorites, name="favorites")
]