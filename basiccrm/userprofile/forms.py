from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder': 'Ваш логин',
        'class': 'bg-forms'
    }))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'placeholder': 'Ваш пароль',
        'class': 'bg-forms'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder': 'Ваш логин',
        'class': 'bg-forms'
    }))
    email = forms.CharField(label="", widget=forms.EmailInput(attrs={
        'placeholder': 'Ваш электронный адрес',
        'class': 'bg-forms'
    }))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'placeholder': 'Ваш пароль',
        'class': 'bg-forms'
    }))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите пароль',
        'class': 'bg-forms'
    }))
