from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CharacterListCreateSerializer, AlterStatusSerializer, UpdateCharSerializer, UpgradeCharSerializer, ExperienceSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from .models import Character
from users.models import User
from trinity_dice.permissions import IsCharOwnerOrReadOnlyPermissions, MasterPermissions, AllowToUpgradeChar
from utils.mixins import SerializerByMethodMixin
from .mixins import UpdateStatusMixin

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

class AlterStatusView(UpdateStatusMixin, UpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = AlterStatusSerializer
    permission_classes = [MasterPermissions] 

class UpgradeCharView(UpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = UpgradeCharSerializer
    permission_classes = [MasterPermissions, AllowToUpgradeChar]
    
    def perform_update(self, serializer):
        char_id = self.kwargs["pk"]
        char = Character.objects.get(pk=char_id)
        points = char.__dict__["level_up_points"] - 1
        serializer.save(level_up_points=points)

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

        


