from rest_framework.generics import (
    ListCreateAPIView, RetrieveDestroyAPIView, UpdateAPIView
)
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from .models import Item
from bonus.models import Bonus
from systems.models import System

from bonus.serializers import BonusSerializer
from .serializers import ItemPostSerializer, ItemGetSerializer

from trinity_dice.permissions import MasterPermissions
from utils.mixins import SerializerByMethodMixin


class ListCreateItemsView(
    SerializerByMethodMixin,
    ListCreateAPIView,
    PageNumberPagination
):
    permission_classes = [MasterPermissions]
    serializer_map = {
        'GET': ItemGetSerializer,
        'POST': ItemPostSerializer,
    }

    def perform_create(self, serializer):
        system = get_object_or_404(System, pk=self.kwargs['system_id'])
        serializer.save(system=system)

    def get_queryset(self):
        system = get_object_or_404(System, pk=self.kwargs['system_id'])
        return Item.objects.filter(system=system)

class RetrieveDestroyItemsView(RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemPostSerializer

    permission_classes = [MasterPermissions]

class ApplyBonusView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemPostSerializer

    def perform_update(self, serializer):
        bonus_id = self.kwargs["bonus_id"]
        bonus = get_object_or_404(Bonus, pk=bonus_id)
        serializer.save(bonus=bonus)

class RemoveBonusView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemPostSerializer

    def perform_update(self, serializer):
        bonus_id = self.kwargs["bonus_id"]
        item_id = self.kwargs["item_id"]
        item = Item.objects.get(pk=item_id)
        bonus = Bonus.objects.get(pk=bonus_id)
        item.bonus.remove(bonus)

        serializer.validated_data.get('bonus').remove(bonus)
        serializer.save()
