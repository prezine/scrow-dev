from django.db import models

from config.models import BaseModelWithSoftDelete


class Bank(BaseModelWithSoftDelete):
    account_number = models.CharField(max_length=20, unique=True)
    bank_name = models.CharField(max_length=200)

    def __str__(self):
        return self.account_number
