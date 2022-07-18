from rest_framework import permissions

class AdminPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST" or request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_superuser

class MasterPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_master


class IsCharOwnerOrReadOnlyPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.creator

class UserOrAdminPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj or request.user.is_superuser:
            return True
        return False

class MasterAndOwnerPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.creator_id and request.user.is_master:
            return True
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return False