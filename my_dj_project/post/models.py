from django.db import models
from django.urls import reverse
from django.utils import timezone

from new_app.models import CustomerUser


class Tag(models.Model):
    groups = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.groups}"



class Post(models.Model):
    author = models.ForeignKey(CustomerUser, related_name="posts", on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name="posts", on_delete=models.SET_NULL, null=True)
    title = models.TextField(max_length=30, blank=True)
    image = models.ImageField(upload_to="posts", blank=True)
    date_pub = models.DateTimeField(auto_now=True)
    date_change = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=1000, blank=True)
    price = models.IntegerField(blank=None)  # Цена
    phone_numbers = models.CharField(max_length=11)
    favorites = models.ManyToManyField(CustomerUser, related_name="favorites", blank=True)

    def __str__(self):
        return f"Post from {self.author.username}"

    def get_absolute_url(self):
        return reverse('post:detail', args=(self.id, ))

    def get_favorites(self):
        return self.favorites


class Comment(models.Model):
    author = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_pub = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment from {self.author.username} to {self.post.title}"