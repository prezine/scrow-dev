from django.contrib import admin

from transactions.models import Customer, Product, ProductBacklog


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'email', 'address', 'uid')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'amount', 'product_id', 'type')


class ProductBacklogAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'action')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductBacklog, ProductBacklogAdmin)
