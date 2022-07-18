from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.status import HTTP_200_OK
from rest_framework.views import Response

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

    def destroy(self, request, *args, **kwargs):
        system = self.get_object()
        system.is_active = False
        system.save()
        return Response(
            status=HTTP_200_OK,
            data={
                "detail": 'System deactivated!'
            }
        )

