from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class OnlyAdminsCanDelete(IsAuthenticated):
    """This permission ensures that only admins can delete items."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method != 'DELETE':
            return super().has_permission(request, view)
        return request.user.is_admin
