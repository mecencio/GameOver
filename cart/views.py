from django.shortcuts import render, redirect
from cart.cart import Cart
from products.models import Products
from orders.forms import userOrderForm
from profiles.models import userAddresses
from orders.models import Order, OrderItems
from django.conf import settings

# Create your views here.
def add_to_cart(request, product_id):
    cart = Cart(request)
    try: 
        if cart.cart[str(product_id)]:
            cart.add(product_id, 1, True)
    except:
        cart.add(product_id)
    return render(request, 'cart/menu-cart.html')

def buy_again(request, order_id):
    order = OrderItems.objects.filter(order_id=order_id)
    cart = Cart(request)
    for item in order:
        product = Products.objects.get(id=item.product_id)
        try: 
            if cart.cart[str(product.id)]:
                cart.add(product.id, item.quantity, True)
        except:
            cart.add(product.id, (item.quantity-1), True)
    return render(request, 'cart/menu-cart.html')


def cart(request):
    return render(request, 'cart/cart.html')

def checkout(request):
    if request.user.is_authenticated:
        if not request.session.get(settings.CART_SESSION_ID):
            error = "Para continuar debe tener Articulos en el carro"
            return render(request, 'cart/cart.html', {'error':error})
        else:
            if request.method == 'GET':
                Address = userAddresses.objects.filter(user=request.user)[:1]
                try:
                    Address = userAddresses.objects.get(pk=Address)
                except:
                    Address = {}
                if Address:
                    form = userOrderForm(initial={
                        'first_name': request.user.first_name, 
                        'last_name': request.user.last_name, 
                        'email': request.user.email, 
                        'street':Address.street, 
                        'number': Address.number, 
                        'flat':Address.flat, 
                        'apartment':Address.apartment, 
                        'city':Address.city, 
                        'province':Address.province, 
                        'additionalInfo':Address.additionalInfo, 
                        'code':Address.code,
                        'phone': request.user.profile.phone,
                    })
                else:
                    form = userOrderForm(initial={
                        'first_name': request.user.first_name, 
                        'last_name': request.user.last_name, 
                        'email': request.user.email
                    })
                return render(request, 'cart/checkout.html', {'form':form})
            else:
                cart = Cart(request)
                form = userOrderForm(request.POST)

                if form.is_valid():
                    order = Order.objects.create(
                        user=request.user, 
                        first_name = form.cleaned_data['first_name'], 
                        last_name = form.cleaned_data['last_name'], 
                        email = form.cleaned_data['email'], 
                        street = form.cleaned_data['street'], 
                        number = form.cleaned_data['number'], 
                        flat = form.cleaned_data['flat'], 
                        apartment = form.cleaned_data['apartment'], 
                        city = form.cleaned_data['city'], 
                        province = form.cleaned_data['province'], 
                        additionalInfo = form.cleaned_data['additionalInfo'], 
                        code = form.cleaned_data['code'], 
                        phone = form.cleaned_data['phone'],
                    )

                    if request.POST.get('checkbox') == 'on':
                        userAddresses.objects.create(
                            user=request.user, 
                            street = form.cleaned_data['street'], 
                            number = form.cleaned_data['number'], 
                            flat = form.cleaned_data['flat'], 
                            apartment = form.cleaned_data['apartment'], 
                            city = form.cleaned_data['city'], 
                            province = form.cleaned_data['province'], 
                            additionalInfo = form.cleaned_data['additionalInfo'], 
                            code = form.cleaned_data['code'], 
                        )

                    paid_amount = 0
                    for item in cart:
                        product = item['product']
                        price = product.price
                        quantity = int(item['quantity'])
                        total_price = price * quantity
                        paid_amount += total_price

                        item = OrderItems.objects.create(
                            order=order,
                            product=product,
                            price = price,
                            quantity = quantity,
                            total_price = total_price,
                        )
                    
                    order.paid_amount = paid_amount
                    order.save()
                    
                    Cart(request).clear()
                    return redirect('My profile')
                
                else:
                    errors = form.errors.items()
                    form = userOrderForm()
                    context = {'errors': errors, 'form':form}
                    return render(request, 'cart/checkout.html', context)
    else:
        return redirect('/login')

def hx_menu_cart(request):
    return render(request, 'cart/menu-cart.html')

def hx_cart_total(request):
    return render(request, 'cart/part/cart-total.html')

def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)
    
    product = Products.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)
    
    if quantity:
        quantity = quantity['quantity']
        item = {
            'product' : {
                'id' : product.id,
                'name' : product.name,
                'image': product.image,
                'price' : product.price,
            },
            'total_price': (quantity * product.price),
            'quantity' : quantity,
        }
    else:
        item = None

    context = {'item':item}
    response = render(request, 'cart/part/cart-item.html', context)
    response['HX-Trigger'] = 'update-menu-cart'

    return response