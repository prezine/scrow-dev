from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = (
        'name', 'email', 'phone', 'is_staff', 'is_active', 'country',)
    list_filter = ('is_staff', 'is_active', 'created_at',)
    fieldsets = (
        ('Basic Details', {'fields': (
            'name', 'email','password', 'calling_code', 'phone',
        )}),
        ('Others', {'fields': (
            'gender', 'address', 'country', 'state', 'city', 'photo', 'active_business',)}),
        ('Permissions', {'fields': ('is_staff', 'deleted_at', 'is_active', 'is_activated',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name', 'email', 'calling_code', 'phone', 'password1',
                'password2', 'gender', 'address', 'country', 'state', 'city')}
         ),
    )

    search_fields = ('name', 'email', 'phone',)
    ordering = ('name', 'phone', 'email',)


admin.site.register(User, UserAdmin)
