from django.urls import path

app_name = "app"

urlpatterns = [
    path('', home.as_view(), name="home")
]
