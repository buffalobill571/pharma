from django.contrib import admin
from .models import Product, Category, Feature, Order
from django.contrib.auth.models import Group, User


class FeatureInline(admin.TabularInline):
    model = Feature


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (FeatureInline,)
    list_filter = ('category',)
    list_display = ('id', 'name', 'manufacturer', 'price')
    search_fields = ('name', 'manufacturer')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'email', 'phone', 'price')
    autocomplete_fields = ('purchased_products',)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_header = 'Pharmacareweb'
