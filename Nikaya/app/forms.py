from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','email','first_name','last_name','password','is_admin']
