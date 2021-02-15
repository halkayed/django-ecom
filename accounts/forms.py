from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm


from .models import Profile

User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text= 'Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text= 'Optional.')
    email = forms.EmailField(max_length=100, required=True, help_text= 'Kindly Enter a valid Email')
     
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
        
class ProfileForm(ModelForm):
    address = forms.CharField(max_length=250)

    class Meta:
        model = Profile
        fields = ('address',)
    