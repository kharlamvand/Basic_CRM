from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_CLASS = 'w-full my-4 py-4 px-6 rounded-xl bg-gray-100'


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ваш логин',
        'class': INPUT_CLASS
    }))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        'placeholder': 'Ваш пароль',
        'class': INPUT_CLASS
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={
        'placeholder': 'Ваш логин',
        'class': INPUT_CLASS
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Ваш электронный адрес',
        'class': INPUT_CLASS
    }))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        'placeholder': 'Ваш пароль',
        'class': INPUT_CLASS
    }))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите пароль',
        'class': INPUT_CLASS
    }))
