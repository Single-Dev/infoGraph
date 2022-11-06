from django.urls import path
from .views import *
app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("signup/", signup, name="signup"),
    path("stats/<slug:slug>/", StatsView, name="chart"),
    path("<str:username>", PublicProfileView, name="profile"),
    path("<str:username>/new", NewDashboardView, name="new")
]
