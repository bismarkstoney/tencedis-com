from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomerUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model=CustomerUser
        fields=('username', 'email')
class CustomerUserChangeForm(UserChangeForm):

    class Meta:
        model=CustomerUser
        fields=('username', 'email')