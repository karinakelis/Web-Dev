# api/admin.py

from django.contrib import admin
from .models import Product, Category

# Register Product and Category models to be managed through the Admin panel
admin.site.register(Product)
admin.site.register(Category)
