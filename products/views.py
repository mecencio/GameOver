from django.shortcuts import render
from django.views.generic import DetailView
from products.models import Products

# Create your views here.
class detailProduct(DetailView):
    model = Products
    template_name = 'products/detail-product.html'

    def get_context_data(self, **kwargs):
        context = super(detailProduct, self).get_context_data(**kwargs)
        context['Category'] = Products.objects.filter(category__name = context['object'].category)
        context['Brand'] = Products.objects.filter(brand = context['object'].brand)
        return context

def search_view(request):
    products = Products.objects.filter(name__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'products/search.html', context=context)

def category_search(request):
    products = Products.objects.filter(category__name__icontains = request.GET['search'])
    context = {'products':products}
    return render(request, 'products/search.html', context = context)

def brand_search(request):
    products = Products.objects.filter(brand__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'products/search.html', context = context)

def model_search(request):
    products = Products.objects.filter(model__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'products/search.html', context = context)