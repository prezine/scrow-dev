from django.contrib import admin

from .models import Business, Staff, Role

admin.site.register(Business)
admin.site.register(Role)
admin.site.register(Staff)
