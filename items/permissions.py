from rest_framework.permissions import BasePermission, SAFE_METHODS


class ItemPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        return request.user.is_authenticated and request.user.is_master
