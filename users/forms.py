from django import forms

from users.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'required': 'please enter your email address'})
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class ForgotPasswordForm(forms.Form):
    email = forms.CharField(required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Please enter your email address.")

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("User with this e-mail address does not exist.")

        return cleaned_data


class ForgotResetForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    retype_password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password').lower()
        retype_password = cleaned_data.get('retype_password').lower()

        if not password:
            raise forms.ValidationError("Please enter your password")

        if len(password) < 6:
            raise forms.ValidationError("Password must be above 6 characters.")

        if retype_password != password:
            raise forms.ValidationError("Password and retype password do not match")

        return cleaned_data
