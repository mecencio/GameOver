from django.contrib import admin
from orders.models import Order

# Register your models here.
class ordersAdmin(admin.ModelAdmin):
    id = 'Orden n°'
    list_display = ('first_name', 'last_name', 'id', 'paid', 'paid_amount', 'status')
    search_fields = ['first_name', 'last_name', 'id',]

admin.site.register(Order, ordersAdmin)