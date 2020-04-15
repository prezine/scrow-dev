from rest_framework.permissions import BasePermission


class IsTeamMembersOnly(BasePermission):
    """
    Allows access only to users who are part of a business.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.active_business)
