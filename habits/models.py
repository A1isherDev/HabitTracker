from django.db import models
from colorfield.fields import ColorField
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User  # yoki custom user

class Habits(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="habits"
    )
    title = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')  # qizil rang
    frequency = ArrayField(
        base_field=models.IntegerField(),
        default=list,
        help_text="List of weekdays. Example: [1,2,3,4,5] = Mon–Fri"
    )
    icon = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.title