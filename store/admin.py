from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Columns visible in admin list
    list_display = ['name', 'price', 'category', 'stock']
    # Search box in admin
    search_fields = ['name', 'category']
    # Filter sidebar
    list_filter = ['category']