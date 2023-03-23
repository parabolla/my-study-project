from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.utils.translation import gettext_lazy as _

from new_app.models import CustomerUser


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'placeholder': _('Username'),
        'class': 'form-control',
    }))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'class': 'form-control',
        }),
    )


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ("username", "avatar", "about")
