from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from trinity_dice.permissions import MasterPermissions

from .serializers import SystemSerializer
from .models import System


class ListCreateSystemView(ListCreateAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer

    permission_classes = [MasterPermissions]


class RetrieveDestroySystemView(RetrieveDestroyAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer

    permission_classes = [MasterPermissions]
