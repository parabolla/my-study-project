from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from post.models import Post


def index(request):
    posts = Post.objects.all().order_by("-date_pub")[:10]
    context = {
        "header": "Last ten pub",
        "posts": posts,
    }
    return render(request, "post/index.html", context)


# def all_posts(request):  # Список с фильтром
#     posts = Post.objects.all()
#     context = {
#         "header": "All posts",
#         "posts": posts,
#     }
#     return render(request, 'post/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    header = f"Post: {post.title}"
    context = {
        "header": f"Post: {post.title}",
        "post": post,
    }
    return render(request, "post/post_detail.html", context)


def post_create(request):

    return HttpResponse("Create post")


def post_update(request, post_id):
    return HttpResponse(f"Update post id:{post_id}")


def post_delete(request, post_id):
    return HttpResponse(f"Delete post id: {post_id}")


def favorites(request): #Добавление в избранное
    return HttpResponse(f"add favorites list")
