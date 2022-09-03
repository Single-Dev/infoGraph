from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)


class Countrys(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

class Profile(models.Model):
    # profile_pic = models.ImageField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    bio = models.CharField(max_length=70)
    premium_bio = models.CharField(max_length=140)
    mobile_number = models.IntegerField(default=998)
    country = models.OneToOneField(Countrys, on_delete=models.CASCADE)
    def __str__(self):
        return self.bio


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category_name

class Dashboard(models.Model):
    author = models.OneToOneField(Users, on_delete=models.CASCADE)
    dahboard = models.CharField(max_length=200)
    dashboard_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.dahboard

class Dash_dates(models.Model):
    item = models.CharField(max_length=15)
    item_price = models.IntegerField(default=0)

    def __str__(self):
        return self.item