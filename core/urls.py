from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView , LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("chart.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "chart.views.handler404"
handler500 = "chart.views.handler500"