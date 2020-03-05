import os
from django import template

from business.models import Staff

register = template.Library()


@register.simple_tag
def staff_role(user):
    if user.business:
        try:
            return Staff.objects.get(role__user=user.pk).role
        except Staff.DoesNotExist:
            return None
    return None
