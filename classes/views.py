from rest_framework import generics

from .models import Class
from trinity_dice.permissions import MasterPermissions
from .serializers import ClassesSerializer, ClassListSerializer


# class ListClassView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [MasterPermissions]

#     def get(self, request, system_id):
#         system = get_object_or_404(System, pk=system_id)
#         classes = Class.objects.filter(system=system)

#         serializer = ClassListSerializer(classes, many=True)

#         return Response(serializer.data)


class ListClassView(generics.ListAPIView):
    permission_classes = [MasterPermissions]

    queryset = Class.objects.all()
    serializer_class = ClassListSerializer
    lookup_url_kwarg = "system_id"
    lookup_field = "system"


class GetDeleteClassView(generics.RetrieveDestroyAPIView):
    permission_classes = [MasterPermissions]

    queryset = Class.objects.all()
    serializer_class = ClassesSerializer
