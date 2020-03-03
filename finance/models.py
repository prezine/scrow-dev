from django.db import models

from config.models import BaseModelWithSoftDelete


class Bank(BaseModelWithSoftDelete):
    account_name = models.CharField(max_length=200)
    account_number = models.IntegerField()
    bank = models.CharField(max_length=200)

    def __str__(self):
        return self.account_name
