from django.contrib import admin

from productos.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'price', 
        'description',
    )