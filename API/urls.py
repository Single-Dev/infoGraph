from django.urls import path
from API.views import *

app_name = "api"

urlpatterns =[
    path('users/', UsersApiView, name="users" ),
    path('create-user/', CreateUserViaApi, name="create_user"),
    path('update-user/<int:pk>', UpdateUserViaApi, name="update_user")
]
