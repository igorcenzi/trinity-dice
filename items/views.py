from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import ItemPermissions
from .serializers import ItemSerializer
from .models import Item


class ListCreateItemsView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ItemPermissions]

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class RetrieveDestroyItemsView(RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ItemPermissions]

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

