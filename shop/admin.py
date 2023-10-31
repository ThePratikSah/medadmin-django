from django.contrib import admin
from .models import Category, Product, Brand, ProductVariation


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo_url', 'created', 'updated')


class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'brand', 'prescription_required', 'created', 'updated')
    inlines = (ProductVariationInline,)
    prepopulated_fields = {'sku': ('name',)}
    list_filter = ('categories', 'brand', 'prescription_required')
    raw_id_fields = ['brand']
    search_fields = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'created', 'updated')
