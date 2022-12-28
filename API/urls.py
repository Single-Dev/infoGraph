from django.urls import path
from API.views import *
app_name = "api"

urlpatterns =[
    path('users/', UsersApi, name="users_api" )
]
