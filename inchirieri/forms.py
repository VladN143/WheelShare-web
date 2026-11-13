from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'nickname', 'account_type', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput)

from .models import Car

class MasinaForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'an_fabricatie', 'pret', 'detalii', 'imagine']

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'description']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }