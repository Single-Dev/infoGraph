from django.contrib.auth import get_user_model
from rest_framework import serializers
from chart.models import *

User = get_user_model()

# User API
class UsersApi(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username","email", "first_name", "last_name", "is_organiser", "is_agent",)

# Chart API
class ChartAPi(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = ("id", "author","name", "slug", "caption", "chart_type", "created_on",)

# Element API
class ElementApi(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ("id","post", "title", "value")

class ContactUsApi(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ("id", "name", "email", "subject", "message", "is_view")