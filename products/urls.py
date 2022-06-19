from django.urls import path
from products.views import search_view, detailProduct

# Create your views here.
urlpatterns = [
    path('search-product/', search_view, name = 'Searh product'),
    path('detail-product/<int:pk>/', detailProduct.as_view(), name = 'Detail product'),

]