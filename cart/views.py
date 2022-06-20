from django.shortcuts import render, redirect
from cart.cart import Cart

# Create your views here.
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/menu-cart.html')

def cart(request):
    return render(request, 'cart/cart.html')

def checkout(request):
    if request.user.is_authenticated:
        return render(request, 'cart/checkout.html')
    else:
        return redirect('/login')