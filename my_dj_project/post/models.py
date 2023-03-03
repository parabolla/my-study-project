from django.db import models
from django.utils import timezone

from new_app.models import CustomerUser


class Post(models.Model):
    author = models.ForeignKey(CustomerUser, related_name="posts", on_delete=models.CASCADE)
    title = models.TextField(max_length=30)
    image = models.ImageField(upload_to="posts", blank=True)
    date_pub = models.DateTimeField(auto_now=True)
    date_change = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=1000, blank=True)
    group = models.TextField(max_length=20) # Группа товаров
    favorites = models.ManyToManyField(CustomerUser, related_name="favorites", blank=True) # список избранного
    price = models.IntegerField(max_length=100000)#Цена
    phone_numbers = models.IntegerField(max_length=11)


    def __str__(self):
        return f"Post from {self.author.username}"


# asd