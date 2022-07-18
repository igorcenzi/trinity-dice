from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .mixins import AddItemToInventoryMixin
from items.models import Item
from .serializers import CharacterListCreateSerializer, AlterStatusSerializer, UpdateCharSerializer, UpgradeCharSerializer, ExperienceSerializer, AddItemToInventorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from .models import Character
from users.models import User
from trinity_dice.permissions import IsCharOwnerOrReadOnlyPermissions, MasterPermissions
from utils.mixins import SerializerByMethodMixin

class ListCreateCharView(ListCreateAPIView):
    queryset = Character.objects.filter()
    serializer_class = CharacterListCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
    
    def get_queryset(self):
        owner = get_object_or_404(User, email=self.request.user)
        return Character.objects.filter(creator=owner)

class CharDetailsView(SerializerByMethodMixin, RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_map = {
        'PATCH': UpdateCharSerializer,
        'GET': CharacterListCreateSerializer
    }
    permission_classes = [IsCharOwnerOrReadOnlyPermissions]

class AlterStatusView(UpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = AlterStatusSerializer
    permission_classes = [MasterPermissions]    

class UpgradeCharView(UpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = UpgradeCharSerializer
    permission_classes = [MasterPermissions]

class GainExpView(UpdateAPIView): 
    queryset = Character.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [MasterPermissions]
    
    def perform_update(self, serializer):
        amount_exp = serializer.validated_data["gained_exp"]
        char_id = self.kwargs["pk"]
        char = Character.objects.get(pk=char_id)
        current_exp = char.__dict__["exp_points"]
        max_exp = char.__dict__["max_exp_points"]
        current_level = char.__dict__["level"]
        points = char.__dict__["level_up_points"]
        new_exp = amount_exp + current_exp

        if new_exp >= max_exp:
            max_exp = max_exp * 1.10
            current_level += 1
            new_exp = 0
            points += 1
            serializer.save(exp_points=new_exp, max_exp_points=max_exp, level=current_level, level_up_points=points)

        else:
            serializer.save(exp_points=new_exp)


class AddNewItemToInventoryView(AddItemToInventoryMixin, UpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = AddItemToInventorySerializer
    permission_classes = [MasterPermissions]
    lookup_url_kwarg = 'char_id'
    
    def perform_update(self, serializer):
        character = Character.objects.get(id=self.kwargs['char_id'])
        item = Item.objects.get(id=self.kwargs['item_id'])
        item.characters.add(character)
        item.save()