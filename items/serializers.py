from rest_framework import serializers

from .models import Item
"""
from systems.models import System
from inventories.models import Inventory
from classes.models import Class
"""


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'precision': { 'min_value': 0, 'max_value': 20 },
            'min_level': { 'min_value': 0 }
        }

    def create(self, validated_data):
        """
        system = get_object_or_404(System, id=validated_data["system"])
        inventories = get_object_or_404(Inventory, id=validated_data["inventories"])
        classes = get_object_or_404(Class, id=validated_data["classes"])

        validated_data["system"] = system
        validated_data["inventories"] = inventories
        validated_data["classes"] = classes
        """

        return Item.objects.create(**validated_data)

