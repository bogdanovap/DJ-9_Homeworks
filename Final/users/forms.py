from django import forms

from .models import User


class SignupForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ('username', 'email', 'password')
        labels = {
            'username': 'Имя пользователя',
            'email': 'E-mail',
            'password': 'Пароль',
        }
        help_texts = {
            'username': '',
        }
        widgets = {
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(),
        }
