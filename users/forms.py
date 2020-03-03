from django import forms

from users.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'required': 'please enter your email address'})
    password = forms.CharField(widget=forms.PasswordInput, required=True)
