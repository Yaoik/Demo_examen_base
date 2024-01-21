from typing import Any
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import CustomUser
from django import forms



class CustomUserLogin(AuthenticationForm):
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'fio']
        
    error_messages = {
        "invalid_login": _(
            "Неверный Email или Пароль"
        ),
        "inactive": _("This account is inactive."),
    }
    
class CustomUserRegister(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ['email', 'fio']
        
    error_messages = {
        "password_mismatch": _("Пароли не совпадают."),
    }
    
    email = forms.CharField(error_messages={'required': 'Введите правильный Email', "incomplete": 'Введите правильный Email', 'invalid':'Введите правильный Email'}, label='Email адрес*')
    fio = forms.CharField(label='ФИО*')

    password1 = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        error_messages={'required': 'Пароль должен быть длинее 8 символов', "incomplete": 'Пароль должен быть длинее 8 символов', 'invalid':'Пароль должен быть длинее 8 символов'}
    )
    password2 = forms.CharField(
        label=_("Повторите Пароль"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
