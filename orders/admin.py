from django.contrib import admin
from orders.models import Order, OrderItems

# Register your models here.
class OrderItemsInline(admin.TabularInline):
    model = OrderItems

class ordersAdmin(admin.ModelAdmin):
    id = 'Orden n°'
    list_display = ('first_name', 'last_name', 'id', 'paid', 'paid_amount', 'status', 'create_at')
    list_filter = ['status', 'create_at',]
    search_fields = ['first_name', 'last_name', 'id',]
    inlines = [
        OrderItemsInline,
    ]

admin.site.register(Order, ordersAdmin)