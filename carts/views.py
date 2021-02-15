from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


from products.models import Products
from .models import Cart,CartItems
from .forms import CartItemForm
# Create your views here.


@login_required
def add_to_cart(request):

    if int(request.user.cart.id) == int(request.POST['cart']):
        form = CartItemForm(request.POST)
        if form.is_valid():
            form.update()
    else:
        print('Miss match !!!!!!!!!!!!')

    return redirect('list_products')


@login_required
def remove_from_cart(request, product_id):
    item = get_object_or_404(Products, pk=product_id)
    cart = Cart.objects.get(user = request.user)
    cart.items.remove(item)
    
    return redirect('cart')


@login_required
def clear_cart(request):
    cart = Cart.objects.get(user=request.user)
    items = cart.items.all()
    for item in items:
        cart.items.remove(item)

    return redirect('cart')
        
        


@login_required
def cart(request):

    cart = request.user.cart
    cartItems = CartItems.objects.filter(cart=cart)
    
    return render(request,'cart/cart.html', {'items' : cartItems, 'total_price' : cart.total_price()})

    
    