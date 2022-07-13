from rest_framework import serializers

from classes.models import Class


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"
