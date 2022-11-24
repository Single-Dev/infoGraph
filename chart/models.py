from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
from PIL import Image

class MyUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    following = models.ManyToManyField("self", blank=True, related_name="followers", symmetrical=False)
    email_confirmed = models.BooleanField(default=False)

class Profile(models.Model):
    class Meta:
        verbose_name = "My Profile"
        verbose_name_plural = "Profile"
    custom_user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    image = models.ImageField(default="profile/profile.jpg", upload_to="profile")
    bio = models.CharField(max_length=100, null=True, blank=True, default="")
    is_online = models.BooleanField(default=False)
    def __str__(self):
        return f"id: {self.id}, {self.custom_user}"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Chart(models.Model):
    PIE = "Pie"
    COLUMN = "Column"
    CHART_CHOICES = [
        (PIE, "Pie Chart"),
        (COLUMN, "Column Chart")
    ]
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name='chart' )
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    caption = models.TextField(max_length=700)
    created_on = models.DateTimeField(("date joined"), default=timezone.now)
    chart_type = models.CharField(max_length=15,choices=CHART_CHOICES, default=PIE)
    def __str__(self):
        return self.name

class Element(models.Model):
    post = models.ForeignKey(Chart,on_delete=models.CASCADE,related_name='element')
    title = models.CharField(max_length=80)
    value = models.IntegerField(default=0)

    def __str__(self):
        return f"title: {self.title}, post: {self.post}"

# class Category(models.Model):
#     category_name = models.CharField(max_length=30)

#     def __str__(self):
#         return f"id: {self.id}, name:{self.category_name}"

class ContactUs(models.Model):
    TAKLIF = "Taklif"
    SHIKOYAT = "Shikoyat"
    CONTACT_CHOICES = [
        (TAKLIF, "Taklif"),
        (SHIKOYAT, "Shikoyat")
    ]
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=8, choices=CONTACT_CHOICES, default=TAKLIF)
    message = models.TextField(max_length=700)
    is_view = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}, subject: {self.subject}"
    