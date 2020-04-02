from django.db import models

from config.models import BaseModel

GENDER_CHOICE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Not sure', 'Not sure')
)


class Customer(BaseModel):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    address = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default='Not sure')


TRANSACTION_STATUS = (
    ('in progress', 'in progress'),
    ('terminated', 'terminated'),
    ('completed', 'completed')
)


class Transaction(BaseModel):
    product_name = models.CharField(max_length=300)
    product_quantity = models.IntegerField()
    delivery_date = models.DateField()
    currency = models.CharField(max_length=100, default='USD')
    amount = models.DecimalField(max_digits=17, decimal_places=2)
    terms = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=TRANSACTION_STATUS, default='in progress')
    transaction_id = models.CharField(max_length=200)
