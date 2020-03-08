from django import forms

from business.models import Staff
from finance.models import Bank


class BankDetailsForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'


class WorkersForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
