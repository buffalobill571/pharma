from django.contrib import admin
from .models import Product, Category, Feature


class FeatureInline(admin.TabularInline):
    model = Feature


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (FeatureInline,)
    list_filter = ('category',)
    list_display = ('id', 'name', 'manufacturer', 'price')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
