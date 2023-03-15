from django.urls import path
from post.views import *
# для входа внутрь поста
app_name = "post"

urlpatterns = [
    path('', index, name="index"),
    # path("all_posts/", all_posts, name="all_posts"),
    path("post_detail/<int:post_id>/", post_detail, name="detail"),
    path("subscribe/", subcribe_view, name="subscribe"),
    path("post_create/", post_create, name="create"),
    path("post_update/<int:post_id>/", UpdatePostView.as_view(), name="update"),
    path("post_delete/<int:post_id>/", DeletePostView.as_view(), name="delete"),
    path("favorites/<int:post_id>/", favorites, name="favorites"),
    path("comment/<int:post_id>/", post_comment, name="comment"),
    path("delete-comment/<int:comment_id>/", DeleteCommentView.as_view(), name="delete_comment"),
]