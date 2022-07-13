from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from classes.models import Class
from classes.serializers import ClassesSerializer


class ListCreateClassView(
    generics.ListCreateAPIView,
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Class.objects.all()
    serializer_class = ClassesSerializer


class DeleteClassView(
    generics.DestroyAPIView,
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Class.objects.all()
    serializer_class = ClassesSerializer


class RetrieveUpdateClassView(
    generics.RetrieveUpdateAPIView,
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Class.objects.all()
    serializer_class = ClassesSerializer
