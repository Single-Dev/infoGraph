from django.urls import path
from .views import *
app_name = "app"

urlpatterns = [
    path('', Home.as_view(), name="home"),
    # path('<str:name>/dash/', test, name="test")
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('<slug:slug>/comment/', new_comment, name="new_comment")
]
