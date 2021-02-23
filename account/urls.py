from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import RegistrationView, ActivationVIew, SigninView,SuccessfulRegistrationView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('succerssful_registration/', SuccessfulRegistrationView.as_view(), name='succesful-registration'),
    path('activation/', ActivationVIew.as_view(), name='activation'),
    path('login/', SigninView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]