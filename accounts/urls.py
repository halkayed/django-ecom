from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from .views import signup, activate_email




LoginView.template_name = 'accounts/login.html'


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/',  LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:uid>/<str:token>/', activate_email, name='activate_email'),
    path('password-reset', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
