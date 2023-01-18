
from rest_framework import generics

from .models import Class
from trinity_dice.permissions import MasterPermissions
from .serializers import ClassListSerializer

class ListClassView(generics.ListAPIView):
    permission_classes = [MasterPermissions]

    queryset = Class.objects.all()
    serializer_class = ClassListSerializer
    lookup_url_kwarg = "system_id"
    lookup_field = "system"


class GetDeleteClassView(generics.RetrieveDestroyAPIView):
    permission_classes = [MasterPermissions]

    queryset = Class.objects.all()
    serializer_class = ClassListSerializer
