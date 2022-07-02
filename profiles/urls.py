from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from profiles.views import my_profile_view, edit_information_view, address_view, add_address_view, delete_address_view, edit_address_view, my_purchases_view, delete_image

urlpatterns = [
    path('', my_profile_view, name='My profile'),
    path('delete-image', delete_image, name='delete image'),
    path('addresses/', address_view, name='Address'),
    path('my-purchases/', my_purchases_view, name='my purchases'),
    path('add-address/', add_address_view, name='add-address'),
    path('edit-address/<int:address_id>',edit_address_view, name='edit-address'),
    path('delete-address/<int:address_id>/', delete_address_view, name='delete-address'),
    path('my-profile/my-information', edit_information_view, name='Edit information'),
]