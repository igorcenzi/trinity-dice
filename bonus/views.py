from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import Bonus
from .serializers import BonusSerializer
from trinity_dice.permissions import MasterPermissions

class BonusView(ListCreateAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer
    permission_classes = [MasterPermissions]

class BonusDetailView(RetrieveDestroyAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer
    permission_classes = [MasterPermissions]
