from rest_framework import serializers

from classes.models import Class


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"
        read_only_fields = ["id"]


class ClassCreateGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"
        read_only_fields = ["id", "system"]
