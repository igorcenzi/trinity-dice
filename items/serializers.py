from rest_framework import serializers
from django.shortcuts import get_object_or_404

from bonus.serializers import BonusSerializer
from bonus.models import Bonus
from .models import Item
from classes.models import Class

class ItemClassSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Class
        fields = ['name']

class ItemPostSerializer(serializers.ModelSerializer):
    system = serializers.CharField(source='system.name', read_only=True)
    classes = ItemClassSerializer(many=True)

    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['id', 'characters', 'bonus']
        extra_kwargs = {
            'precision': { 'min_value': 0, 'max_value': 20 },
            'min_level': { 'min_value': 0 }
        }

    def create(self, validated_data: dict):
        class_data = validated_data.pop("classes")
        item = Item.objects.create(**validated_data)
        for klass in class_data:
            klass_name = klass['name']
            my_class = get_object_or_404(Class, name=klass_name)
            item.classes.add(my_class)

        return item

class ItemGetSerializer(serializers.ModelSerializer):
    system = serializers.CharField(source='system.name')
    classes = ItemClassSerializer(many=True)

    class Meta:
        model = Item
        fields = '__all__'

class ApplyBonusSerializer(serializers.ModelSerializer):
    bonus = BonusSerializer(many=True)
    classes = ItemClassSerializer(many=True)

    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['id', 'characters', 'bonus']
        extra_kwargs = {
            'precision': { 'min_value': 0, 'max_value': 20 },
            'min_level': { 'min_value': 0 }
        }

    def update(self, instance, validated_data):
        bonus_id = self.context["bonus_id"]
        bonus = get_object_or_404(Bonus, pk=bonus_id)
        instance.bonus.add(bonus)
        return super().update(instance, validated_data)

class RemoveBonusSerializer(serializers.ModelSerializer):
    bonus = BonusSerializer(many=True)
    classes = ItemClassSerializer(many=True)

    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['id', 'characters', 'bonus']
        extra_kwargs = {
            'precision': { 'min_value': 0, 'max_value': 20 },
            'min_level': { 'min_value': 0 }
        }
    
    def update(self, instance, validated_data):
        bonus_id = self.context["bonus_id"]
        bonus = get_object_or_404(Bonus, pk=bonus_id)
        instance.bonus.remove(bonus)
        return super().update(instance, validated_data)