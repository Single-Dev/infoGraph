from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)


class Lyrics(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    lyrics = models.TextField(max_length=7000)

    def __str__(self):
        return f"post by {self.author}"