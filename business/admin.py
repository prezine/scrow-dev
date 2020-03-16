from django.contrib import admin

from .models import Business, TeamMember, BusinessVerification, StaffInvite

admin.site.register(Business)
admin.site.register(TeamMember)
admin.site.register(BusinessVerification)
admin.site.register(StaffInvite)
