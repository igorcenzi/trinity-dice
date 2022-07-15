from webbrowser import get
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CharacterListCreateSerializer

from rest_framework.generics import ListCreateAPIView

from .models import Character

from users.models import User


class ListCreateCharView(ListCreateAPIView):
    queryset = Character.objects.filter()
    serializer_class = CharacterListCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        owner = get_object_or_404(User, email=self.request.user)
        return Character.objects.filter(user=owner)
    