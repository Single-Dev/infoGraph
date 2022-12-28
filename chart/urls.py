from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView 
from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("signup/", signup, name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logoutView, name="logout"),
    path("settings/delete/user/", deleteUser, name="delete_user"),
    path("<str:username>", ProfileView, name="profile"),
    path("follow/<str:author>/",followToggle, name="follow"),
    path("settings/password_change/", password_change, name="password_change"),
    path("settings/", settings, name="settings"),
    path("new/", NewChartView, name="new"),
    path("stats/<slug:slug>/", ChartView, name="chart"),
    path("pin/<str:slug>/", ChartPinUnpinView, name="chart_pin_unpin"),
    path("like/<str:slug>/", LikeToggle, name="like"),
    path("edit/<str:slug>/", UpdateChartView, name="update_chart"),
    path("delete/<str:slug>/", deleteChartView, name="delete_chart"),
    path("edit/<str:slug>/<int:pk>", UpdateElementView, name="edit_element"),
    path("delete/<str:slug>/<int:pk>", deleteElementView, name="delete_element"),
    path("result/", SearchView, name="results"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='pages/settings/password_resest_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="pages/settings/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='pages/settings/password_reset_complete.html'), name='password_reset_complete'),      
    path("settings/verify-request/", VerifyRequestView, name="verify_request_view"),
    path("submit-success/", SuccessView.as_view(), name="success_view"),
]
