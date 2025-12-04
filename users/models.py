from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model, get_user

# Create your models here.



class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    def __str__(self):
        return self.username
    