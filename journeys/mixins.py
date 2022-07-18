from rest_framework.response import Response
from characters.models import Character
from django.shortcuts import get_object_or_404

class SerializerByMethodMixin:
    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)

class AddCharToJourneyMixin:
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        character = get_object_or_404(Character, pk = self.kwargs["char_id"])

        return Response({"detail": f'{character.name} has been added to {instance.title}'})

class RemoveCharFromJourneyMixin:
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        character = get_object_or_404(Character, pk = self.kwargs["char_id"])

        return Response({"detail": f'{character.name} has been removed from {instance.title}'})