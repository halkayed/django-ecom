from django.shortcuts import redirect
from django.urls import path
from .views import products,product_details, add_product, edit_product


def home(request):
    return redirect('products/')

urlpatterns = [
    path('', home, name = 'home'),
    path('products/',products, name='list_products'),
    path('products/add', add_product, name = 'add_product'),
    path('products/edit/<pk>', edit_product, name = 'edit_product'),
    path('products/<pk>', product_details,name = 'product_description'),
]