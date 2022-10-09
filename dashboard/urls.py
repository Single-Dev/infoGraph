from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path('', LyricsApiView, name="home")
]
