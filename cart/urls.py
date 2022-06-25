from django.urls import path
from cart.views import add_to_cart, cart, checkout, hx_menu_cart, hx_cart_total, update_cart

urlpatterns = [
    path('', cart, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='Add to cart'),
    path('checkout/', checkout, name='checkout'),
    path('menu-cart/', hx_menu_cart, name="Menu cart"),
    path('cart-total/', hx_cart_total, name="Cart total"),
    path('update-cart/<int:product_id>/<str:action>/', update_cart, name="update_cart"),

]
