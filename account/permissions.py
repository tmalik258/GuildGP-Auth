from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthenticatedUserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False
        if view.basename in ["user"]:
            return bool(request.user and request.user.is_authenticated)
        return False

    def has_permission(self, request, view):
        if view.basename in ["user"]:
            if request.user.is_anonymous:
                return False
            return bool(request.user and request.user.is_authenticated)
        return False
