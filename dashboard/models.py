from django.db import models
from django.contrib.auth.models import AbstractUser
# from PIL import Image

class MyUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

# class Profile(models.Model):
#     class Meta:
#         verbose_name = "My Profile"
#         verbose_name_plural = "Profile"
#     custom_user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
#     image = models.ImageField(default="arrivals5.png", upload_to="profile")
#     bio = models.CharField(max_length=100, default="bio", null=True, blank=True)
#     card_number = models.IntegerField(default=2500, null=True,blank=True)
#     address = models.CharField(max_length=200, null=True, blank=True)
#     mobile_number = models.IntegerField(default=998931742328, null=True, blank=True)
    


#     def save(self, *args, **kwargs):
        # super(Profile, self).save(*args, **kwargs)

        # img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

class Dashboard(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name='tanla' )
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    descraption = models.TextField(max_length=700)
    active = models.BooleanField(default=True)
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