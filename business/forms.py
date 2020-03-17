from django import forms

from business.models import TeamMember
from finance.models import Bank


class BankDetailsForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'


class WorkersForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'
