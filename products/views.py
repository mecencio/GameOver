from django.shortcuts import render
from django.views.generic import DetailView
from django.db.models import Q
from products.models import Category, Products

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
    categories = Category.objects.all()
    products = Products.objects.all()
    brands = []
    model = []

    for product in products:
        brands.append(product.brand)
        model.append(product.model)
    brands = set(brands)
    model = set(brands)

    active_category = request.GET.get('category', '').lower()
    # Filtro los prod por categoría (en caso de buscar por categoría)
    if active_category:
        products = products.filter(category__name__icontains = active_category)

    active_brand = request.GET.get('brand', '')
    # Filtro los prod por marca (en caso de buscar por marca)
    if active_brand:
        products = products.filter(brand__icontains = active_brand)

    active_model = request.GET.get('model', '')
    # Filtro los prod por modelo (en caso de buscar por modelo)
    if active_model:
        products = products.filter(model__icontains = active_model)

    query = request.GET.get('search', '')
    if query:
        products = products.filter(Q(name__icontains = query) | Q(brand__icontains = query) | Q(model__icontains = query))

    context = {
        'categories':categories,
        'products':products,
        'active_category':active_category,
        'active_brand':active_brand,
        'active_model':active_model,
        'brands':brands,
        'model':model,
    }
    return render(request, 'products/search.html', context)