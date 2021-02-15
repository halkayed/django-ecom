from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

class tokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(user.is_active) + str(timestamp)

confirm_email_token_genrator = tokenGenerator()


def send_confirmation_email(request, user):
    token = confirm_email_token_genrator.make_token(user)
    uid = user.pk
    
    domain = get_current_site(request)
    
    subject = 'Activate you account'
    #link = str(domain)+'/'+str(uid)+'/'+str(token)
    context = {'uid':uid, 'token':token, 'user':user, 'domain':domain}
    message = render_to_string('accounts/confirmation-email.html', context=context)
    
    user.email_user(subject, message)



    

