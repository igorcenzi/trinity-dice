from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from trinity_dice.permissions import MasterPermissions
from .serializers import ItemSerializer
from .models import Item


class ListCreateItemsView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    permission_classes = [MasterPermissions]

class RetrieveDestroyItemsView(RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    permission_classes = [MasterPermissions]

