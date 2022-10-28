from .models import *
from django import forms

class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = "__all__"

class AddElementForm(forms.ModelForm):
    class Meta:
        model = AddElement
        fields = "__all__"