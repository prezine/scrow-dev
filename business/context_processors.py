from business.models import Staff


def user_role(request):
    if request.user.is_authenticated:
        if request.user.business:
            try:
                staff = Staff.objects.get(business=request.user.business.pk, role__user=request.user.pk)
            except Staff.DoesNotExist:
                return {'user_role': None, 'business_pk': ''}

            return {'user_role': staff, 'business_pk': request.user.business.pk}

    return {'user_role': None, 'business_pk': ''}
