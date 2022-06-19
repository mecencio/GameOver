from django.contrib import admin
from products.models import Category, Products

# Register your models here.
# categories
# class productInline(admin.TabularInline):
#     model = Products

# class CategoryAdmin(admin.ModelAdmin):
#     inlines = [
#         productInline,
#     ]

admin.site.register(Category)

# products
class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'model', 'category', 'quantity', 'inStock')
    search_fields = ['name', 'brand', 'model', 'category', 'quantity',]

admin.site.register(Products, productAdmin)
