from rest_framework import permissions


class isMasterOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if "is_superuser" in request.user:
            return True

        return request.user.is_master
