from django.urls import path

from .views import check_out, order_success

urlpatterns = [
    path('orders/checkout/', check_out, name='check_out'),
    path('orders/success/', order_success, name='order_success'),
]