from django.urls import path
from API.views import *

app_name = "api"

urlpatterns =[
    path('', home, name="home"),
    path('users/', UsersApiView, name="users" ),
    path("profiles/", ProfileApiView, name="profile"),
    path('create-user/', CreateUserViaApi, name="create_user"),
    path('update-user/<int:pk>', UpdateUserViaApi, name="update_user"),
    path('profile/<int:pk>', SingleProfileApiView, name="profile_id"),
    path('<str:username>', SingleUserApi, name="single_user"),
    path('charts/', ChartApiView, name="charts"),
    path("chart/<str:slug>/", SingleChartApi, name="single_chart"),
    path("elements/", ElementApiView, name="elems"),
    path("requests/", ContactUsApiView, name="contact"),
    path("create-request/", CreateRequestViaApi, name="create_request"),
    path("requests/<int:pk>/", SingleRequestApi, name="request"),
    path("update-requests/<int:pk>/", UpdateRequestApi, name="request"),
]
