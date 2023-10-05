from django import forms
from .models import UserProfile

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'phone_number', 'hire_date']
