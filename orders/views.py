from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Order, OrderItems
from .forms import OrderForm

from carts.models import Cart, CartItems

# Create your views here.


@login_required
def check_out(request):
    
    if request.user.cart.items.count() == 0:
        return redirect('home')
    else:
        
        if request.method == 'GET':
            
            form = OrderForm.cast_from_profile(request)
            return render(request, 'orders/checkout.html', {'form':form})
        
        else:
            form = OrderForm(request.POST)
            if form.is_valid():
                
                if form.save_items(request):
                    return redirect('order_success')
            
            else:
                print('Miss Match!!!!!!!!')
            
            return redirect('home')
            


def order_success(request):
    return render(request, 'orders/success.html')