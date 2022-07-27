from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class Vehicle_Ads_Form(forms.ModelForm):
    class Meta:
        model = Vehicle_Ads
        fields = '__all__'

class UserCreation(UserCreationForm):
    email = forms.EmailField()
    contact_number= forms.IntegerField(max_value=10)

    class Meta:
        model= User
        fields=['username','email','contact_number','password1','password2']