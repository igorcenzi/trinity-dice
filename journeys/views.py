from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListCreateAPIView
from journeys.mixins import SerializerByMethodMixin
from journeys.serializers import CreateSerializer, ListSerializer
from systems.models import System
from .models import Journey

# Create your views here.
class ListCreateJourneyView(SerializerByMethodMixin, ListCreateAPIView):
    queryset = Journey.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = "system_id"
    serializer_map = {
        'GET': ListSerializer,
        'POST': CreateSerializer,
    }

    def perform_create(self, serializer):
        system = get_object_or_404(System, pk=self.kwargs["system_id"])
        creator = self.request.user
        serializer.save(system=system, creator=creator)