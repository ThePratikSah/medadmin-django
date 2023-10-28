from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo_url', 'created', 'updated')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'price', 'selling_price', 'prescription_required', 'created', 'updated')
    prepopulated_fields = {'sku': ('name',)}
    list_filter = ('selling_price', 'prescription_required', 'created', 'updated')

