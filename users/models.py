from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(null=True,blank=True, max_length=30)
    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.title