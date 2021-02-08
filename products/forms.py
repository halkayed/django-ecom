from django.forms import ModelForm
from .models import Products


class AddProduct(ModelForm):
    class Meta:
        model = Products
        fields = ('brand','title', 'description','price', 'image')
