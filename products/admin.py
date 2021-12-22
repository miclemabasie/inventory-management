from django.contrib import admin
from .models import Category, Product, Purchase, Store


admin.site.register(Category)
admin.site.register(Purchase)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity', 'reorder_quantity', 'active', 'created']
    list_editable = ['price', 'active']
    list_filter = ['name', 'created']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
    prepopulated_fields = {"slug": ("name",)}
    

    