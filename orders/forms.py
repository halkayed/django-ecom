from django import forms
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist

from .models import Order, OrderItems
from carts.models import Cart,CartItems


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('send_address',)
        
        
    def save_items(self, request):
        
        order = Order(user=request.user, send_address=self.data['send_address'])
        order.save()
        
        cart = request.user.cart
        try:
            cartItems = CartItems.objects.filter(cart=cart)
        
            for cart_item in cartItems:
            
                orderItems = OrderItems(order=order)
                orderItems.item = cart_item.item
                orderItems.qty = cart_item.qty
                orderItems.save()
                
            cartItems.delete()
            return True
        
        except Exception:

            OrderItems.objects.filter(order=order).delete()
            order.delete()
            
            print("Sorry order deleted")
            return False

            
            
    def cast_from_profile(request):
        
        form = OrderForm()
        form.initial['send_address'] = str(request.user.profile.address)
        
        return form