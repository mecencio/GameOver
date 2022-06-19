from django.urls import path
from cart.views import add_to_cart

urlpatterns = [
    path('add-to-cart/<int:product_id>/', add_to_cart, name='Add to cart'),
    
]
