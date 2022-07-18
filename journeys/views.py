from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveAPIView
import characters
from characters.models import Character
from journeys.exceptions import CharacterAdd, JourneyEndedError
from journeys.mixins import SerializerByMethodMixin
from journeys.serializers import CreateSerializer, ListCharactersSerializer, ListSerializer, UpdateEndedSerializer, UpdateStartedSerializer
from systems.models import System
from rest_framework.views import Response, status
from trinity_dice.permissions import MasterAndOwnerPermissions, MasterPermissions
from .models import Journey
from datetime import datetime
# from integrations.executor import integrate

class ListCreateJourneyView(SerializerByMethodMixin, ListCreateAPIView):
    permission_classes = [MasterPermissions]
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

class UpdateStartedJourneyView(RetrieveUpdateAPIView):
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
        # players = journey.players
        # num_array = []
        # for id_char in players:
        #     char = Character.objects.get(pk=id_char)
        #     user = char.user
        #     num = user["phone"]
        #     num_array.add(num)

        # print(30 * "*", num_array, 30 * "*")
        # # integrate(num_array)

class UpdateEndedJourneyView(RetrieveUpdateAPIView):
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
    queryset=Journey.objects.all()
    serializer_class = CreateSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = "journey_id"

class RetrieveAndUpdateAddJourneyCharactersView(RetrieveUpdateAPIView):
    permission_classes = [MasterAndOwnerPermissions]
    serializer_class = CreateSerializer
    queryset=Journey.objects.all()
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
            # return Response({"detail": f'Add {character.name} to the {journey.title} journey!'})
            raise CharacterAdd()

# class RetrieveAndUpdateDelJourneyCharactersView(RetrieveUpdateAPIView):
#     permission_classes = [MasterAndOwnerPermissions]
#     serializer_class = ListSerializer
#     queryset=Journey.objects.all()
#     lookup_field = 'pk'
#     lookup_url_kwarg = "journey_id"

#     def perform_update(self, serializer):
#         journey = get_object_or_404(Journey, pk=self.kwargs["journey_id"])
#         character = get_object_or_404(Character, pk=self.kwargs["char_id"])
#         print(journey.__dict__)
#         new_list_characters = filter(lambda char: char.id != character.id, journey.players)
#         journey.players = new_list_characters
#         journey.save()
#         serializer.save(players=journey.players)


class RetrieveJourneyCharactersView(RetrieveAPIView):
    serializer_class = ListCharactersSerializer
    queryset = Journey.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = "journey_id"
