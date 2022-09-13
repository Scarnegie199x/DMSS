from django.db import models
from django.contrib.auth.models import AbstractUser
from profanity.validators import validate_is_profane

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30,
                                unique=True,
                                verbose_name = "Username",
                                validators=[validate_is_profane],
                                )
    dm = models.BooleanField(default=True, verbose_name = "Dungeon Master")
    dungeon_name = models.CharField(max_length=30, blank=False, verbose_name = "Dungeon name", validators=[validate_is_profane])
    email = models.EmailField(max_length=255, unique=True, verbose_name = "Email Address")
