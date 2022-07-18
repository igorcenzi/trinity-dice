from rest_framework import serializers
from journeys.models import Journey
from systems.models import System


class CreateSerializer(serializers.ModelSerializer):
    system = serializers.CharField(source='system.name', read_only=True)

    class Meta:
        model = Journey
        read_only_fields=["id", "status", "creator", "started_at", "ended_at", "players"]
        fields = ["id", "title", "description", "min_level", "max_level", "max_players", "status", "system", "creator", "started_at", "ended_at", "players"]


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = "__all__"

class UpdateStartedSerializer(serializers.ModelSerializer):
    system = serializers.CharField(source='system.name', read_only=True)
    class Meta:
        model = Journey
        read_only_fields = ["id", "title", "description", "min_level", "max_level", "max_players", "system", "creator", "ended_at", "players"]
        fields = ["id", "title", "description", "min_level", "max_level", "max_players", "status", "system", "creator", "started_at", "ended_at", "players"]

class UpdateEndedSerializer(serializers.ModelSerializer):
    system = serializers.CharField(source='system.name', read_only=True)
    class Meta:
        model = Journey
        read_only_fields = ["id", "title", "description", "min_level", "max_level", "max_players", "system", "creator", "started_at", "players"]
        fields = ["id", "title", "description", "min_level", "max_level", "max_players", "status", "system", "creator", "started_at", "ended_at", "players"]

class ListCharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        read_only_fields = ["players"]
        fields = ["players"]
        depth = 1