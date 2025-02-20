from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','username','email','phone_number','password1','password2']

class CustomLoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

