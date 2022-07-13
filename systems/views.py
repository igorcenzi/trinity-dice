from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from .serializers import SystemSerializer
from .models import System


class ListCreateSystemView(ListCreateAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer

class RetrieveDestroySystemView(RetrieveDestroyAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer

