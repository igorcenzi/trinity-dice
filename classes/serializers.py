from rest_framework import serializers

from classes.models import Class

# from systems.serializers import SystemSerializer


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"
        read_only_fields = ["id"]


class ListSerializer(serializers.ModelSerializer):
    # system = SystemSerializer(read_only=True)

    class Meta:
        model = Class
        fields = "__all__"
        read_only_fields = ["id", "system"]
