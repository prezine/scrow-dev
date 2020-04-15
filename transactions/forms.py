from django import forms

from transactions.models import Product


class ProductUpdateForm(forms.ModelForm):
    description = forms.CharField(required=True, error_messages={'required': 'Please provide description of product.'})

    class Meta:
        model = Product
        fields = ('name', 'description', 'amount', 'image')
        error_messages = {
            'name': {
                'required': 'Product name is required.'
            },
            'amount': {
                'required': 'Enter amount',
                'invalid': 'Enter valid amount without comma separation or space'
            }
        }


class StoreForm(ProductUpdateForm):
    image = forms.ImageField(required=True, error_messages={'required': 'Upload a valid image for your product'})

    class Meta:
        model = Product
        fields = ('name', 'quantity', 'description', 'amount', 'image')
        error_messages = {
            'name': {
                'required': 'Product name is required.'
            },
            'quantity': {
                'required': 'Enter product quantity.'
            },
            'amount': {
                'required': 'Enter amount',
                'invalid': 'Enter valid amount without comma separation or space'
            }
        }

