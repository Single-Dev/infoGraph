from django.urls import path
from API.views import *

app_name = "api"

urlpatterns =[
    path('', home, name="home"),
    path('users/', UsersApiView, name="users" ),
    path('create-user/', CreateUserViaApi, name="create_user"),
    path('update-user/<int:pk>', UpdateUserViaApi, name="update_user"),
    path('<str:username>', SingleUserApi, name="single_user"),
    path('charts/', ChartApiView, name="charts"),
]
