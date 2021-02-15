from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum, F


from products.models import Products
# Create your models here.

User = get_user_model()


class Cart(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    items = models.ManyToManyField(Products, through='CartItems', related_name='items')
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.user)


    def total_price(self):
        return CartItems.objects.filter(cart=self).aggregate(total = Sum(F('qty')*F('item__price')))['total']

    
@receiver(post_save, sender=User)
def create_cart(sender, instance ,created, **kwargs):
    if created:
        Cart.objects.create(user = instance)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty  = models.PositiveIntegerField(default=1)