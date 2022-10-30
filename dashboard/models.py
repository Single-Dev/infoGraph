from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)


class Dashboard(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    descraption = models.TextField(max_length=700)
    
    def __str__(self):
        return self.name

class AddElement(models.Model):
    post = models.ForeignKey(Dashboard,on_delete=models.CASCADE,related_name='qoshish')
    title = models.CharField(max_length=80)
    value = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    # created_on = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['created_on']

    def __str__(self):
        return f"id: {self.id}, title: {self.title}"