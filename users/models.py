from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='users_images', null=True, blank=True)
    user_type = models.CharField(max_length=10, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username
