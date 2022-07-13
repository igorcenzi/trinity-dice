from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from classes.models import Class
from classes.permissions import isMasterOrAdmin
from classes.serializers import ClassesSerializer


class ListCreateClassView(
    generics.ListCreateAPIView,
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isMasterOrAdmin]

    queryset = Class.objects.all()
    serializer_class = ClassesSerializer


class GetDeleteClassView(
    generics.RetrieveDestroyAPIView,
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isMasterOrAdmin]

    queryset = Class.objects.all()
    serializer_class = ClassesSerializer
