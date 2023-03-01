from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomerUser(AbstractUser):
    birth_date = models.DateField(_("birth date"), blank=True, null=True)
    avatar = models.ImageField(upload_to="profile")
    about = models.TextField(max_length=500, blank=True)


    def __str__(self):
        return str(self.username)


