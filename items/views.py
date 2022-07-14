from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from trinity_dice.permissions import MasterPermissions
from .serializers import ItemSerializer
from .models import Item
from django.shortcuts import get_object_or_404
from bonus.models import Bonus
from bonus.serializers import BonusSerializer

class ListCreateItemsView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    permission_classes = [MasterPermissions]

class RetrieveDestroyItemsView(RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    permission_classes = [MasterPermissions]

class ApplyBonusView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_update(self, serializer):
        bonus_id = self.kwargs["bonus_id"]
        bonus = get_object_or_404(Bonus, pk=bonus_id)
        serializer.save(bonus=bonus)

class RemoveBonusView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_update(self, serializer):
        bonus_id = self.kwargs["bonus_id"]
        item_id = self.kwargs["item_id"]
        item = Item.objects.get(pk=item_id)
        bonus = Bonus.objects.get(pk=bonus_id)
        item.bonus.remove(bonus)

        serializer.validated_data.get('bonus').remove(bonus)
        serializer.save()
