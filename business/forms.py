from django import forms
from finance.models import Bank


class BankDetailsForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'
