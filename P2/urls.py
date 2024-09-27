from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app-coder/', include('app_coder.urls')), #redirige al urls.py de app_coder
]
