from django.urls import path
from .views import *
app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    # path('<str:name>/dash/', test, name="test")
    path('<int:pk>-<slug:slug>/', post_detail, name='post_detail'),
    path('<int:pk>-<slug:slug>/comment/', new_comment, name="new_comment")
]
