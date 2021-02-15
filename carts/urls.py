from django.urls import path
from .views import cart, add_to_cart, remove_from_cart, clear_cart



urlpatterns = [
    path('cart/', cart, name='cart'),
    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<product_id>', remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', clear_cart, name='clear_cart'),
]