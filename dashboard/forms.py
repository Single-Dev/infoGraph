from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = "__all__"

class AddElementForm(forms.ModelForm):
    class Meta:
        model = AddElement
        fields = ("title", "value")