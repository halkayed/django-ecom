from django.db import models
from django.contrib.auth import get_user_model


from products.models import Products


User = get_user_model()
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    items = models.ManyToManyField(Products, related_name='order_items', through='OrderItems')
    orderDate = models.DateTimeField(auto_now=True)
    send_address = models.CharField(max_length=250)
    
    
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()