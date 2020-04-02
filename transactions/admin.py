from django.contrib import admin

from transactions.models import Transaction, Customer

admin.site.register(Transaction)
admin.site.register(Customer)
