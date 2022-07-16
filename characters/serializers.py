from rest_framework import serializers
from .models import Character
from journeys.models import Journey
from classes.models import Class


class JourneyTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = ["title"]

class AlterStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ["status"]
        read_only_fields = ["id", "name", "birth_place", "age", "race", "description", "class", "level", "journey", "creator"]

class ExperienceSerializer(serializers.ModelSerializer):
    gained_exp = serializers.IntegerField(write_only=True)

    class Meta:
        model = Character
        fields = ["gained_exp", "id", "name", "birth_place", "age", "race", "description", "class_name", "level","level_up_points", "exp_points", "max_exp_points", "journey", "user"]
        read_only_fields = ["id", "name", "birth_place", "age", "race", "description", "class_name", "level", "level_up_points", "exp_points", "max_exp_points", "journey", "user"]

class UpdateCharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ["name", "age", "description"]

class UpgradeCharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"
        read_only_fields = ["id", "name", "birth_place", "race", "age", "description", "class", "status", "exp_points", "max_exp_points", "level_up_points" "level", "class", "journey", "creator"]


class CharacterListCreateSerializer(serializers.ModelSerializer):
    journey = JourneyTitleSerializer(read_only=True)

    classes = serializers.CharField(max_length=50, write_only=True)

    class_name= serializers.SerializerMethodField(read_only=True)

    creator_id = serializers.PrimaryKeyRelatedField(source="user_id", read_only=True)

    class Meta:
        model = Character
        fields = [
            "id",
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
            "classes",
            "class_name",
            "journey",
            "creator_id",
        ]
        read_only_fields = [
            "exp_points",
            "max_exp_points",
            "level_up_points",
            "level"
        ]

    def create(self, validated_data: dict):
        class_data = validated_data.pop("classes")
        class_obj, _ = Class.objects.get_or_create(name=class_data)
        return Character.objects.create(**validated_data, class_name=class_obj)

    def get_class_name(self, obj):
        id = obj.__dict__.get('class_name_id')
        classes = Class.objects.get(pk=id)
        return classes.name