from django.urls import path
from .views import *
app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("signup/", signup, name="signup"),
    path("<str:username>", ProfileView, name="profile"),
    path("f/<str:author>/",followToggle, name="follow"),
    path("new/", NewChartView, name="new"),
    path("stats/<slug:slug>/", ChartView, name="chart"),
    path("edit/<str:slug>/", UpdateChartView, name="update_chart"),
    path("delete/<str:slug>/", deleteChartView, name="delete_chart"),
    path("edit/<str:slug>/<int:pk>", UpdateElementView, name="edit_element"),
    path("delete/<str:slug>/<int:pk>", deleteElementView, name="delete_element"),
]
