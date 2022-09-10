from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    dm = models.BooleanField(default=True, verbose_name = "Dungeon Master")
    dungeon_name = models.CharField(max_length=30, blank=False, verbose_name = "Dungeon name")
    email = models.EmailField(max_length=255, unique=True, verbose_name = "Email Address")
