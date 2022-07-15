from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CharacterListCreateSerializer

from rest_framework.generics import ListCreateAPIView

from .models import Character


class ListCreateCharView(ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterListCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
