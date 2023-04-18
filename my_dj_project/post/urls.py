from django.contrib.sitemaps.views import index
from django.urls import path
from .views import *

from .views import subcribe_view, post_detail, post_create, UpdatePostView, DeletePostView, favorites, \
    post_comment, DeleteCommentView

# для входа внутрь поста
app_name = "post"

urlpatterns = [
    path('', index, name="index"),
    path('auto/', auto, name="auto"),
    path('flats/', flats, name="flats"),
    path("post_detail/<int:post_id>/", post_detail, name="detail"),
    path("subscribe/", subcribe_view, name="subscribe"),
    path("post_create/", post_create, name="create"),
    path("post_update/<int:post_id>/", UpdatePostView.as_view(), name="update"),
    path("post_delete/<int:post_id>/", DeletePostView.as_view(), name="delete"),
    path("favorites/<int:post_id>/", favorites, name="favorites"),
    path("comment/<int:post_id>/", post_comment, name="comment"),
    path("delete-comment/<int:comment_id>/", DeleteCommentView.as_view(), name="delete_comment"),
]