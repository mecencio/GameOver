from django.urls import path
from about.views import privacy_policy_view, cancel_request_view, delete_cancel_request_view, contact_us_view, about_us_view, faq_view

urlpatterns = [
    path('', about_us_view, name='about us'),
    path('privacy-policy/', privacy_policy_view, name='privacy policy'),
    path('contact-us/', contact_us_view, name='contact us'),
    path('faq', faq_view, name='faq'),
    path('cancel-buy/', cancel_request_view, name='cancel buy'),
    path('delete-cancel-buy/<int:request_id>', delete_cancel_request_view, name='delete cancel request'),
]