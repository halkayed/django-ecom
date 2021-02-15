from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .models import Products
from .forms import AddProduct
from carts.forms import CartItemForm
from carts.models import Cart,CartItems
from store.tools import is_superuser
# Create your views here.

def products(request):
    return render(request, 'products/products-list.html', {'products' :Products.objects.all()})

'''
    @TODO fix to allow unregistered users to go through inventory
'''
@login_required
def product_details(request, pk):
    product = get_object_or_404(Products,pk=pk)
    cart = request.user.cart
    
    try:
        cartItem = CartItems.objects.get(item=product, cart=cart)
    except ObjectDoesNotExist:
        cartItem = CartItems(item=product, cart=cart, qty=1)

    form = CartItemForm(instance=cartItem)
    #cartItem = CartItems.objects.get(item=product, cart=cart)
    #form = CartItemForm()
    return render(request, 'products/product-details.html', {'product':product, 'form': form})


@login_required
@is_superuser
def add_product(request):
    #if request.user.is_superuser and request.user.is_authenticated:
    if request.method == 'GET':
        product_form = AddProduct()
    else:
        product_form = AddProduct(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return render(request, 'products/product-add-successful.html')
    return render(request, 'products/product-add.html', {'product_form': product_form})
    #else:
    #    return redirect('/products/')

@login_required
@is_superuser
def edit_product(request, pk):
    #if request.user.is_superuser and  request.user.is_authenticated:
    product = get_object_or_404(Products, pk=pk)
    
    if request.method == 'GET':
        product_form = AddProduct(instance=product)
    else:
        product_form = AddProduct(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return render(request, 'products/product-add-successful.html', {'added_product': request.POST['title']})
        
    return render(request, 'products/product-add.html', {'product_form': product_form})
    #else:
    #    return redirect('home')