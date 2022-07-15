from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from journeys.mixins import SerializerByMethodMixin
from journeys.serializers import CreateSerializer, ListSerializer
from .models import Journey

# Create your views here.
class ListCreateJourneyView(SerializerByMethodMixin, ListCreateAPIView):
    queryset = Journey.objects.all()
    serializer_map = {
        'GET': ListSerializer,
        'POST': CreateSerializer,
    }