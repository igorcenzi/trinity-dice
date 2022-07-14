from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from classes.models import Class
from classes.permissions import isMasterOrAdminOrReadOnly
from classes.serializers import ClassesSerializer, ClassListSerializer

# from systems.serializers import SystemSerializer


# from systems.models import System


class ListClassView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isMasterOrAdminOrReadOnly]

    def get(self, request, system_id):
        system = get_object_or_404(System, pk=system_id)
        classes = Class.objects.filter(system=system)

        serializer = ClassListSerializer(classes, many=True)

        return Response(serializer.data)


# class ListClassView(generics.ListAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [isMasterOrAdminOrReadOnly]

#     queryset = Class.objects.all()
#     serializer_class = ClassListSerializer
#     lookup_url_kwarg = "system_id"
#     lookup_field = "id"

# def get_queryset(self):
#     user = self.request.user
#     return user.accounts.all()

# def get(self, request, system_id, *args, **kwargs):
#     system = get_object_or_404(System, pk=system_id)
#     return Response({system_id})


class GetDeleteClassView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isMasterOrAdminOrReadOnly]

    queryset = Class.objects.all()
    serializer_class = ClassesSerializer
