from django.db import models

from config.models import BaseModelWithSoftDelete


class Bank(BaseModelWithSoftDelete):
    account_name = models.CharField(max_length=200)
    account_number = models.CharField(max_length=20, unique=True)
    bank_name = models.CharField(max_length=200)
    bvn = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.account_name
