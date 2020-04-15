from django.db import models

from business.models import Business
from config.models import BaseModel, BaseModelWithSoftDelete
from users.models import User
from utils.files import file_upload_path

GENDER_CHOICE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Not sure', 'Not sure')
)
TRANSACTION_STATUS = (
    ('in progress', 'in progress'),
    ('terminated', 'terminated'),
    ('completed', 'completed')
)
TYPE = (
    ('normal', 'normal'),
    ('product', 'product')
)


class Customer(BaseModel):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    address = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default='Not sure')
    uid = models.CharField(max_length=50)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)


class Product(BaseModelWithSoftDelete):
    name = models.CharField(max_length=300)
    quantity = models.IntegerField()
    delivery_date = models.DateField(null=True, blank=True)
    amount = models.DecimalField(max_digits=17, decimal_places=2)
    currency = models.CharField(max_length=100, default='USD')
    terms = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    product_id = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=TRANSACTION_STATUS, default='in progress')
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    type = models.CharField(choices=TYPE, default='normal', max_length=20)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=file_upload_path.product_image_upload_path, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)


class ProductBacklog(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.TextField()
