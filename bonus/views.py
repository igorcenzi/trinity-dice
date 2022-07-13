from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import Bonus
from .serializers import BonusSerializer

class BonusViews(ListCreateAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

class BonusDetailView(RetrieveDestroyAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer
