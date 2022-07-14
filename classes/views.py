from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from classes.models import Class
from classes.permissions import isMasterOrAdminOrReadOnly
from classes.serializers import ClassCreateGetSerializer, ClassesSerializer


class ListCreateClassView(
    generics.ListCreateAPIView,
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isMasterOrAdminOrReadOnly]

    queryset = Class.objects.all()
    serializer_class = ClassCreateGetSerializer

    def perform_create(self, serializer):
        serializer.save(system=self.request.data)


class GetDeleteClassView(
    generics.RetrieveDestroyAPIView,
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isMasterOrAdminOrReadOnly]

    queryset = Class.objects.all()
    serializer_class = ClassesSerializer
