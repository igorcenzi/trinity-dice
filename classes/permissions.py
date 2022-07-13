from rest_framework import permissions


class isMasterOrAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if "is_superuser" in request.user:
            return True

        return request.user.is_master
