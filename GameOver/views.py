from django.shortcuts import render
from products.models import Products

# Create your views here.
def index(request):
    available_products = Products.objects.filter(inStock = True)
    context = {'available_products':available_products}
    return render(request, 'index.html', context=context)
