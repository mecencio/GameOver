from django.urls import path
from cart.views import add_to_cart, cart, checkout

urlpatterns = [
    path('add-to-cart/<int:product_id>/', add_to_cart, name='Add to cart'),
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    
]
