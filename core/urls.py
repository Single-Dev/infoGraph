from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView , LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("chart.urls")),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
