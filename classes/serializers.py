from rest_framework import serializers

from classes.models import Class

from systems.models import System


class SystemNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ["name"]

class ClassListSerializer(serializers.ModelSerializer):
    system = SystemNameSerializer(read_only=True)

    class Meta:
        model = Class
        fields = "__all__"
