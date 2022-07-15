from rest_framework import serializers

from classes.models import Class

from .models import Character

from journeys.models import Journey


class JourneyTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = ["title"]


class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["name"]


class CharacterListCreateSerializer(serializers.ModelSerializer):
    journey = JourneyTitleSerializer(read_only=True)

    classes = serializers.CharField(max_length=50, write_only=True)

    class_name = ClassNameSerializer(read_only=True)

    creator_id = serializers.PrimaryKeyRelatedField(source="user_id", read_only=True)

    class Meta:
        model = Character
        fields = [
            "name",
            "birth_place",
            "race",
            "description",
            "status",
            "health_points",
            "mana_points",
            "intelligence_points",
            "strength_points",
            "stamina_points",
            "dexterity_points",
            "attack_points",
            "defense_points",
            "exp_points",
            "max_exp_points",
            "level_up_points",
            "level",
            "class_name",
            "classes",
            "journey",
            "creator_id",
        ]
        read_only_fields = [
            "exp_points",
            "max_exp_points",
            "level_up_points",
            "level",
        ]

    def create(self, validated_data: dict):
        print()
        class_data = validated_data.pop("classes")
        class_obj, _ = Class.objects.get_or_create(name=class_data)
        return Character.objects.create(**validated_data, class_name=class_obj)
