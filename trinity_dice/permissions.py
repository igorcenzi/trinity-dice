from rest_framework import permissions
from rest_framework import exceptions


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
    
class AllowToUpgradeChar(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.level_up_points <= 0:
            raise exceptions.PermissionDenied({"detail": "This character does not have enough points to upgrade."})
        return obj.level_up_points > 0