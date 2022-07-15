from rest_framework import serializers
from django.shortcuts import get_object_or_404


from .models import Item
from systems.models import System
"""
from characters.models import Character
from classes.models import Class
from bonus.models import Bonus
"""


class ItemPostSerializer(serializers.ModelSerializer):
    system = serializers.CharField(source='system.name', read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['id', 'characters', 'classes', 'bonus']
        extra_kwargs = {
            'precision': { 'min_value': 0, 'max_value': 20 },
            'min_level': { 'min_value': 0 }
        }
        depth = 1

class ItemGetSerializer(serializers.ModelSerializer):
    system = serializers.CharField(source='system.name')

    class Meta:
        model = Item
        fields = '__all__'

