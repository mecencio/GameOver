from django.urls import path
from products.views import search_view, category_search, brand_search, model_search, detailProduct

# Create your views here.
urlpatterns = [
    path('search-product/', search_view, name = 'Searh product'),
    path('search-category-product/', category_search, name = 'Category products'),
    path('search-brand-product/', brand_search, name = 'Search brand products'),
    path('search-model-product/', model_search, name = 'Search model products'),
    path('detail-product/<int:pk>/', detailProduct.as_view(), name = 'Detail product'),

]