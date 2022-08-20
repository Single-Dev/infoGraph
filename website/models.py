from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
