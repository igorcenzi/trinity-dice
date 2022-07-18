from rest_framework.generics import (
    ListCreateAPIView, RetrieveDestroyAPIView, UpdateAPIView
)
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from .models import Item
from systems.models import System

from .serializers import ApplyBonusSerializer, RemoveBonusSerializer, ItemPostSerializer, ItemGetSerializer

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
    serializer_class = ApplyBonusSerializer

    def get_serializer_context(self):
        context = super(ApplyBonusView, self).get_serializer_context()
        context.update({"bonus_id": self.kwargs["bonus_id"]})
        return context    

class RemoveBonusView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = RemoveBonusSerializer

    def get_serializer_context(self):
        context = super(RemoveBonusView, self).get_serializer_context()
        context.update({"bonus_id": self.kwargs["bonus_id"]})
        return context  
