from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseBadRequest
from django.contrib.auth.models import User


from .models import Profile
from .forms import SignUpForm, ProfileForm
from .utils import send_confirmation_email, confirm_email_token_genrator
# Create your views here.


def signup(request):
    if request.method == 'POST':
        
        signupForm = SignUpForm(request.POST)
        profileForm = ProfileForm(request.POST)
        
        if signupForm.is_valid() and profileForm.is_valid():
        
            user = signupForm.save()
            user.is_active = False
            user.save()
            
            profile = user.profile
            profile.address = profileForm.data['address']
            profile.save()
                
            send_confirmation_email(request, user)
            return render(request, 'accounts/confirmation-email-sent.html', {'user':user})
    else:
        signupForm = SignUpForm()
        profileForm = ProfileForm()
        
    return render(request, 'accounts/signup.html', {'signupForm':signupForm, 'profileForm':profileForm})



def activate_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)
    
    if confirm_email_token_genrator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('login')
    else:
        return HttpResponseBadRequest('Bad Token')