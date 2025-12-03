from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(("first_name"), max_length=50)
    last_name = models.models.CharField(("last_name"), max_length=50)
    profile_picture = models.ImageField()
    