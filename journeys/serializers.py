from rest_framework import serializers
from journeys.models import Journey
from systems.models import System


class ListCreateJourneySerializer(serializers.ModelSerializer):
    system = serializers.CharField(source="system.name", read_only=True)

    class Meta:
        model = Journey
        fields = [
            "id",
            "title",
            "description",
            "min_level",
            "max_level",
            "max_players",
            "status",
            "system",
            "creator",
            "started_at",
            "ended_at",
            "players",
        ]
        read_only_fields = ["status", "creator", "started_at", "ended_at", "players"]


class UpdateStartedSerializer(serializers.ModelSerializer):
    system = serializers.CharField(source="system.name", read_only=True)

    class Meta:
        model = Journey
        fields = [
            "id",
            "title",
            "description",
            "min_level",
            "max_level",
            "max_players",
            "status",
            "system",
            "creator",
            "started_at",
            "ended_at",
            "players",
        ]
        read_only_fields = [
            "title",
            "description",
            "min_level",
            "max_level",
            "max_players",
            "system",
            "creator",
            "ended_at",
            "players",
        ]


class UpdateEndedSerializer(serializers.ModelSerializer):
    system = serializers.CharField(source="system.name", read_only=True)

    class Meta:
        model = Journey
        fields = [
            "id",
            "title",
            "description",
            "min_level",
            "max_level",
            "max_players",
            "status",
            "system",
            "creator",
            "started_at",
            "ended_at",
            "players",
        ]
        read_only_fields = [
            "title",
            "description",
            "min_level",
            "max_level",
            "max_players",
            "system",
            "creator",
            "started_at",
            "players",
        ]


class ListCharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = ["players"]
        read_only_fields = ["players"]
        depth = 1
