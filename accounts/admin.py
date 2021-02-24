from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerUserChangeForm, CustomUserCreationForm
from .models import CustomerUser

@admin.register(CustomerUser)
class CustomeUserAdmin(UserAdmin):
    add_form= CustomUserCreationForm
    form=CustomerUserChangeForm
    model=CustomerUser
    list_display=['email', 'username']
