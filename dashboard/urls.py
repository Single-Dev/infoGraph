from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("<slug:slug>/", DashboardView, name="dashboard_view"),
    path("<slug:slug>/comment", AddElementView, name="add_element")
]
