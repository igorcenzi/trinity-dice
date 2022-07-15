from rest_framework import permissions


class AdminPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST" or request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser


class MasterPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_master


class UserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False


class UserOrAdminPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj or request.user.is_superuser:
            return True
        return False
