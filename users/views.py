from rest_framework import generics
from users.serializers import UserSerializer
from .models import User
from .permissions import AdminPermissions, UserOrAdminPermissions
# Create your views here.
class ListCreateUserView(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AdminPermissions]
  
class ListUserDetailsView(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [UserOrAdminPermissions]
  lookup_url_kwarg = 'user_id'
  lookup_field = 'id'
  
