from django import template

from business.models import TeamMember, Business

register = template.Library()


@register.simple_tag
def staff_role(user):
    if user.active_business:
        try:
            return TeamMember.objects.get(user=user.pk, business=user.active_business.pk).role
        except TeamMember.DoesNotExist:
            return None
    return None
