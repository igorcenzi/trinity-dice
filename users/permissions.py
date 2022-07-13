from rest_framework.permissions import BasePermission

class AdminPermissions(BasePermission):
  def has_permission(self, request, view):
    if request.method == 'POST':
      return True
    return request.user.is_superuser
  
class MasterPermissions(BasePermission):
  def has_permission(self, request, view):
    if request.method == 'POST':
      return True
    return request.user['is_master']

  
class UserPermissions(BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.user == obj:
      return True
    return False
  
class UserOrAdminPermissions(BasePermission):  
  def has_object_permission(self, request, view, obj):
    if request.user == obj or request.user.is_superuser:
      return True
    return False