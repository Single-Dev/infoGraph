from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class NewChartFrom(forms.ModelForm):
    class Meta:
        model = Chart
        fields = ("name", "slug", "caption")

class NewElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ("title", "value")

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', "username"]

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "bio"]