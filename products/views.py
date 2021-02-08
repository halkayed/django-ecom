from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Products
from .forms import AddProduct


# Create your views here.

def products(request):
    return render(request, 'products/products-list.html', {'products' :Products.objects.all()})

def product_details(request, pk):
    product = get_object_or_404(Products,pk=pk)
    return render(request, 'products/product-details.html', {'product':product})

def add_product(request):
    if request.method == 'GET':
        product_form = AddProduct()
    else:
        product_form = AddProduct(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return render(request, 'products/product-add-successful.html', {'added_product': request.POST['name']})
        
    return render(request, 'products/product-add.html', {'product_form': product_form})


def edit_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    
    if request.method == 'GET':
        product_form = AddProduct(instance=product)
    else:
        product_form = AddProduct(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return render(request, 'products/product-add-successful.html', {'added_product': request.POST['title']})
        
    return render(request, 'products/product-add.html', {'product_form': product_form})