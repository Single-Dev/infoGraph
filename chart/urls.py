from django.urls import path
from .views import *
app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("signup/", signup, name="signup"),
    path("stats/<slug:slug>/", ChartView, name="chart"),
    path("profile/<str:username>/", PublicProfileView, name="profile"),
    path("new/", NewDashboardView, name="new"),
    path("follow/<str:author>/",followToggle, name="followToggle")
]
