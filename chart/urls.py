from django.urls import path
from .views import *
app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("<str:username>", ProfileView, name="profile"),
    path("f/<str:author>/",followToggle, name="follow"),
    path("password_change/", password_change, name="password_change"),
    path("settings/", settings, name="settings"),
    path("new/", NewChartView, name="new"),
    path("signup/", signup, name="signup"),
    path("stats/<slug:slug>/", ChartView, name="chart"),
    path("edit/<str:slug>/", UpdateChartView, name="update_chart"),
    path("delete/<str:slug>/", deleteChartView, name="delete_chart"),
    path("edit/<str:slug>/<int:pk>", UpdateElementView, name="edit_element"),
    path("delete/<str:slug>/<int:pk>", deleteElementView, name="delete_element"),
    path("result/", results, name="results"),
]
