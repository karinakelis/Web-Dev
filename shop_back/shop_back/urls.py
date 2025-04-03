# shop_back/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin panel
    path('api/', include('api.urls')),  # This includes the api URLs under /api/
]
