from django.urls import path
from staff.views import panel_view, add_category, add_product, modify_category_menu, modify_category, delete_category, modify_product_menu, modify_product, delete_product, view_request_to_cancel, edit_request_to_cancel, view_contact_us, edit_contact_us, view_orders

urlpatterns = [
    path('', panel_view, name='staff view'),
    path('add-category/', add_category, name='add category'),
    path('modify-category/', modify_category_menu, name='modify category menu'),
    path('modify-category/<int:category_id>', modify_category, name='modify category'),
    path('delete-category/<int:category_id>/<str:status>/', delete_category, name='delete category'),
    path('add-product/', add_product, name='add product'),
    path('modify-product/', modify_product_menu, name='modify product menu'),
    path('modify-product/<int:product_id>', modify_product, name='modify product'),
    path('delete-product/<int:product_id>/<str:status>/', delete_product, name='delete product'),
    path('request-to-cancel', view_request_to_cancel, name='request to cancel'),
    path('request-to-cancel/edit/<int:request_id>/', edit_request_to_cancel, name='edit request to cancel'),
    path('messages-contact', view_contact_us, name='messages contact'),
    path('messages-contact/edit/<int:message_id>/', edit_contact_us, name='edit message'),
    path('view-orders', view_orders, name='view orders'),
]