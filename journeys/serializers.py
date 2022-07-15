from pyexpat import model
from attr import field
from rest_framework import serializers

from journeys.models import Journey

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        read_only_fields=["id", "status", "creator_id", ]
        fields = ["title", "description", "min_level", "max_level", "max_players", "system"]

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        field = "__all__"

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        read_only_fields = "__all__"