from django import forms
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist


from .models import CartItems

class CartItemForm(ModelForm):
    class Meta:
        model = CartItems
        fields = ('cart','item','qty')
        widgets = {'cart': forms.HiddenInput(), 'item': forms.HiddenInput()}
        
    
    def update(self):
        '''
        if 
            exists update the qty of a cart item
        else
            create new cart item
        '''
        item = self.data['item']
        cart = self.data['cart']
        qty  = self.data['qty']
        
        try:
            cartItem = CartItems.objects.get(item=item,cart=cart)
            cartItem.qty = qty
            cartItem.save()
        except ObjectDoesNotExist: 
            self.save()