from django.urls import path
from profiles.views import my_profile_view, address_view, add_address_view, delete_address_view, edit_address_view, my_purchases_view, delete_image, user_security_view, delete_account_view

urlpatterns = [
    # MY PROFILE
    path('', my_profile_view, name='My profile'),
    path('delete-image', delete_image, name='delete image'),
    # PURCHASES
    path('my-purchases/', my_purchases_view, name='my purchases'),
    # ADDRESS
    path('addresses/', address_view, name='Address'),
    path('add-address/', add_address_view, name='add-address'),
    path('edit-address/<int:address_id>',edit_address_view, name='edit-address'),
    path('delete-address/<int:address_id>/', delete_address_view, name='delete-address'),
    # USER SECURITY
    path('security/', user_security_view, name='user security'),
    path('security/delete-account/<str:status>/', delete_account_view, name='delete account'),
]