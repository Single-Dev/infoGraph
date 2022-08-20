from django.urls import path
from .views import *
app_name = "app"

urlpatterns = [
    path('', Home.as_view(), name="home")
]
