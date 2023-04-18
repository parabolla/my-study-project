from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, UpdateView

from .forms import SubscribeForm, PostForm, CommentPostForm
from .models import Post, Comment, Tag


def index(request):
    posts = Post.objects.all().order_by("-date_pub")[:10]
    context = {
        "header": "Store sale",
        "posts": posts,
    }
    return render(request, "post/index.html", context)


def auto(request):
    posts = Post.objects.all().filter(tag__groups="Cars")
    context = {
        "header": "Groups",
        "posts": posts,
    }
    return render(request, "post/groups.html", context)

def flats(request):
    posts = Post.objects.all().filter(tag__groups="Flats")
    context = {
        "header": "Groups",
        "posts": posts,
    }
    return render(request, "post/flats.html", context)




def subcribe_view(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            return redirect('post:index')
    else:
        form = SubscribeForm()

    context = {
        "header": "Subscribe",
        "form": form
    }

    return render(request, "post/subscribe.html", context)


@login_required
def post_create(request):
    if not request.user.is_authenticated:
        # TODO: перекинуть пользователя на регистрацию
        return redirect('post:index')
    if request.method == "GET":
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post.get_absolute_url())

    context = {
        "header": "Create post",
        "form": form
    }

    return render(request, "post/post_create.html", context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    header = f"Post: {post.title}"
    context = {
        "header": f"Post: {post.title}",
        "post": post,
        "comment_form" : CommentPostForm(),
    }
    return render(request, "post/post_detail.html", context)



class UpdatePostView(UpdateView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "post/post_update.html"
    form_class = PostForm

    def get_success_url(self):
        object = self.get_object()
        return reverse('post:detail', kwargs={'post_id': object})

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            raise PermissionDenied(" You are not the author")

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = f'update post#{self.object.id}'
        return context

def post_update(request, post_id):

    return HttpResponse(f"Update post id:{post_id}")


class DeletePostView(DeleteView):
    model = Post
    pk_url_kwarg = "post_id"
    template_name = "post/post_delete.html"
    success_url = reverse_lazy("post:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = f'delete post#{self.object.id}'
        return context

    @method_decorator(login_required)
    def post(self, *args, **kwargs):
        object = self.get_object()

        if self.request.user == object.author:
            return super().post(*args, **kwargs)
        else:
            raise PermissionDenied("you are not the author of this content")


def favorites(request, post_id):  # Добавление в избранное
    post = get_object_or_404(Post, id=post_id)
    if request.user.is_authenticated:
        if request.user in post.favorites.all():
            post.favorites.remove(request.user)
        else:
            post.favorites.add(request.user)

    return redirect(request.META.get('HTTP_REFERER'), request)


def post_comment(request, post_id):
    if request.method =='POST' and request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        form = CommentPostForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied("You are not the author")


class DeleteCommentView(DeletePostView):
    model = Comment
    pk_url_kwarg = "comment_id"
    template_name = "post/comment_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = f'delete comment#{self.object.id}'
        return context
