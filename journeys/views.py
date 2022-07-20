from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveAPIView
from characters.models import Character
from journeys.exceptions import JourneyEndedError, JourneyStartedError
from journeys.serializers import ListCreateJourneySerializer, ListCharactersSerializer, UpdateEndedSerializer, UpdateStartedSerializer
from systems.models import System
from trinity_dice.permissions import MasterAndOwnerPermissions, MasterPermissions
from .models import Journey
from datetime import datetime
from .mixins import AddCharToJourneyMixin, RemoveCharFromJourneyMixin
# from integrations.executor import integrate

class ListCreateJourneyView(ListCreateAPIView):
    permission_classes = [MasterPermissions]
    serializer_class = ListCreateJourneySerializer
    queryset = Journey.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = "system_id"

    def perform_create(self, serializer):
        system = get_object_or_404(System, pk=self.kwargs["system_id"])
        creator = self.request.user
        serializer.save(system=system, creator=creator)

class StartJourneyView(RetrieveUpdateAPIView):
    permission_classes = [MasterAndOwnerPermissions]
    queryset = Journey.objects.all()
    serializer_class = UpdateStartedSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = "journey_id"

    def perform_update(self, serializer):
        journey = get_object_or_404(Journey, pk=self.kwargs["journey_id"])
        journey.status = "Started"
        journey.started_at = datetime.now()
        journey.save()
        serializer.save(status=journey.status, started_at=journey.started_at)
        # players = Character.objects.filter(journey = journey)
        # num_array = []
        # for char in players:
        #     num = char.creator.phone
        #     num_array.append(num)

        # integrate(num_array)

class EndJourneyView(RetrieveUpdateAPIView):
    permission_classes = [MasterAndOwnerPermissions]
    queryset = Journey.objects.all()
    serializer_class = UpdateEndedSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = "journey_id"

    def perform_update(self, serializer):
        journey = get_object_or_404(Journey, pk=self.kwargs["journey_id"])
        journey.status = "Ended"
        journey.ended_at = datetime.now()
        journey.save()
        serializer.save(status=journey.status, ended_at=journey.ended_at)

class RetrieveAndDeleteJourneyView(RetrieveDestroyAPIView):
    permission_classes = [MasterAndOwnerPermissions]
    queryset = Journey.objects.all()
    serializer_class = ListCreateJourneySerializer
    lookup_field = 'pk'
    lookup_url_kwarg = "journey_id"

class AddCharToJourneyView(AddCharToJourneyMixin, RetrieveUpdateAPIView):
    permission_classes = [MasterAndOwnerPermissions]
    serializer_class = ListCreateJourneySerializer
    queryset = Journey.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = "journey_id"

    def perform_update(self, serializer):
        journey = get_object_or_404(Journey, pk=self.kwargs["journey_id"])
        character = get_object_or_404(Character, pk=self.kwargs["char_id"])
        if journey.status == "Ended":
            raise JourneyEndedError()
        else:
            journey.players.add(character)
            journey.save()

class RemoveCharFromJourneyView(RemoveCharFromJourneyMixin, RetrieveUpdateAPIView):
    permission_classes = [MasterAndOwnerPermissions]
    serializer_class = ListCreateJourneySerializer
    queryset=Journey.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = "journey_id"

    def perform_update(self, serializer):
        journey = get_object_or_404(Journey, pk=self.kwargs["journey_id"])
        character = get_object_or_404(Character, pk=self.kwargs["char_id"])

        if journey.status == "Started":
           raise JourneyStartedError()

        if journey.status == "Ended":
           raise JourneyEndedError()

        else:
           journey.players.remove(character)
           journey.save()

class ListJourneyCharactersView(RetrieveAPIView):
    serializer_class = ListCharactersSerializer
    queryset = Journey.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = "journey_id"
