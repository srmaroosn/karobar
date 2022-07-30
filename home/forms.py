from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model=Customer
        fields='__all__'
        exclude= ['user']

class UserCreation(UserCreationForm):
    email = forms.EmailField()
    contact_number= forms.IntegerField(max_value=10)

    class Meta:
        model= User
        fields=['username','email','contact_number','password1','password2']