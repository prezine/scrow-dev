from django.contrib import admin

from .models import Business, Staff, Role, BusinessVerification, StaffInvite

admin.site.register(Business)
admin.site.register(Role)
admin.site.register(Staff)
admin.site.register(BusinessVerification)
admin.site.register(StaffInvite)
