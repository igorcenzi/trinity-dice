from rest_framework import serializers

from classes.models import Class
from items.models import Item
from .models import System


class SystemClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["name"]


class SystemItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "description"]


class SystemSerializer(serializers.ModelSerializer):
    classes = SystemClassSerializer(many=True)
    items = SystemItemsSerializer(many=True, read_only=True)

    class Meta:
        model = System
        fields = ["id", "name", "dice", "version", "classes", "items", "is_active"]

    def create(self, validated_data: dict):
        class_data = validated_data.pop("classes")
        system = System.objects.create(**validated_data)
        for klass in class_data:
            my_class, _ = Class.objects.get_or_create(**klass)
            system.classes.add(my_class)

        return system
