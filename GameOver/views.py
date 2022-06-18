from django.shortcuts import render
from products.models import products

# Create your views here.
def index(request):
    product = products.objects.filter(inStock = True)
    context = {'product':product}
    return render(request, 'index.html', context=context)
