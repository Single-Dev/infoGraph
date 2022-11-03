from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("signup/", signup, name="signup"),
    path("stats/<slug:slug>/", StatsView, name="stats"),
    path("@<str:username>/", PublicProfileView, name="profile"),
    # path("follow/<str:user_name>", follow_user, name="follow")
]
