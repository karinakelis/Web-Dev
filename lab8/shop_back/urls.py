from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shop_back.api.urls')),
    path("", home),
]
