from django.urls import path
from staff.views import panel_view, add_category

urlpatterns = [
    path('', panel_view, name='staff view'),
    path('add-category/', add_category, name='add category'),
]