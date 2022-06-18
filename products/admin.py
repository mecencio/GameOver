from django.contrib import admin
from products.models import category, products

# Register your models here.
# categories
admin.site.register(category)

# products
class productadmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'model', 'category', 'quantity', 'inStock')
    search_fields = ['name', 'brand', 'model', 'category', 'quantity',]

admin.site.register(products, productadmin)
