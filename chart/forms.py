from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    def clean_username(self):
        username = self.cleaned_data.get('username')  # get the username data
        lowercase_username = username.lower()         # get the lowercase version of it

        return lowercase_username

class ChartFrom(forms.ModelForm):
    class Meta:
        model = Chart
        fields = ("name", "chart_type","slug", "caption")
    
    def clean_slug(self):
        slug = self.cleaned_data.get("slug")
        lowercase_slug = slug.lower()

        return lowercase_slug

class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ("title", "value")

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', "username", "email"]

    def clean_username(self):
        username = self.cleaned_data.get('username')  # get the username data
        lowercase_username = username.lower()         # get the lowercase version of it

        return lowercase_username

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "bio"]

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["name", "email", "subject", "message"]