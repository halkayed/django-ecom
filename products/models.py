from django.db import models
from django.urls import reverse
# Create your models here.

class Products(models.Model):
    brand = models.CharField(max_length= 100)
    title = models.CharField(max_length= 100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(null=False)
    image = models.ImageField(upload_to = 'products/',null=True, default='no_image.jpeg')
    
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_description',args=(self.id,))