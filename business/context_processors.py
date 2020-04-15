from django.db.models import Q

from business.models import TeamMember, Business


def user_role(request):
    if request.user.is_authenticated:
        if request.user.active_business:
            try:
                staff = TeamMember.objects.get(business=request.user.active_business.pk, user=request.user.pk)
            except TeamMember.DoesNotExist:
                return {'user_role': None, 'business_pk': ''}

            return {'user_role': staff, 'business_pk': request.user.active_business.pk}

    return {'user_role': None, 'business_pk': ''}


def user_businesses(request):
    if request.user.is_authenticated:
        if request.user.active_business:
            memberships = TeamMember.objects.filter(Q(user=request.user.pk), ~Q(business=request.user.active_business.pk))
            return {'user_businesses': [Business.objects.get(pk=membership.business.pk) for membership in memberships]}
    return {'user_businesses': ()}
