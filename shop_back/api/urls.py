# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

# Initialize the router
router = DefaultRouter()

# Register the viewsets with the router
router.register(r'products', ProductViewSet)  # Route for /products/
router.register(r'categories', CategoryViewSet)  # Route for /categories/

# URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Includes all the routes defined in the router
]
