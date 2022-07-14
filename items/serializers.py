from rest_framework import serializers
from django.shortcuts import get_object_or_404


from .models import Item
"""
from systems.models import System
from characters.models import Character
from classes.models import Class
from bonus.models import Bonus
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
        characters = get_object_or_404(Character, id=validated_data["characters"])
        classes = get_object_or_404(Class, id=validated_data["classes"])
        bonus = get_object_or_404(Bonus, id=validated_data["bonus"])

        validated_data["system"] = system
        validated_data["characters"] = characters
        validated_data["classes"] = classes
        validated_data["bonus"] = bonus
        """

        return Item.objects.create(**validated_data)
