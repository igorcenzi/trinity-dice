from rest_framework import serializers

from classes.models import Class
from .models import System


class SystemClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['name']

class SystemSerializer(serializers.ModelSerializer):
    classes = SystemClassSerializer(many=True)

    class Meta:
        model = System
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1

    def create(self, validated_data: dict):
        class_data = validated_data.pop("classes")
        system = System.objects.create(**validated_data)
        for klass in class_data:
            my_class, _ = Class.objects.get_or_create(**klass)
            system.classes.add(my_class)

        return system

