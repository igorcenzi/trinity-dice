from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from items.models import Item

class AddItemToInventoryMixin:
  def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        item = get_object_or_404(Item, pk=self.kwargs["item_id"])    

        return Response({"detail": f"Added {item.name} to {instance.name} inventory!"})

class RemoveItemFromInventoryMixin:
  def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        item = get_object_or_404(Item, pk=self.kwargs["item_id"])    

        return Response({"detail": f"Removed {item.name} from {instance.name} inventory!"})