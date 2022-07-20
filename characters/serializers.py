from rest_framework import serializers
from .models import Character
from journeys.models import Journey
from classes.models import Class
from classes.serializers import Class
from items.serializers import ItemGetSerializer


class JourneyTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = ["title"]


class AlterStatusSerializer(serializers.ModelSerializer):
    journey = JourneyTitleSerializer(read_only=True)

    class Meta:
        model = Character
        fields = ["name", "status"]
        read_only_fields = [
            "name",
            "birth_place",
            "age",
            "race",
            "description",
            "class",
            "level",
            "creator",
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    journey = JourneyTitleSerializer(read_only=True)

    gained_exp = serializers.IntegerField(write_only=True)

    class Meta:
        model = Character
        fields = [
            "id",
            "name",
            "birth_place",
            "age",
            "race",
            "description",
            "class_name",
            "gained_exp",
            "level",
            "level_up_points",
            "exp_points",
            "max_exp_points",
            "journey",
            "creator",
        ]
        read_only_fields = [
            "id",
            "name",
            "birth_place",
            "age",
            "race",
            "description",
            "class_name",
            "level",
            "level_up_points",
            "exp_points",
            "max_exp_points",
            "journey",
            "creator",
        ]


class UpdateCharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ["id", "name", "age", "description"]


class UpgradeCharSerializer(serializers.ModelSerializer):
    journey = JourneyTitleSerializer(read_only=True)

    class Meta:
        model = Character
        fields = "__all__"
        read_only_fields = [
            "id",
            "name",
            "birth_place",
            "race",
            "age",
            "description",
            "class",
            "status",
            "level",
            "level_up_points",
            "exp_points",
            "max_exp_points",
            "class",
            "journey",
            "creator_id",
        ]


class CharacterListCreateSerializer(serializers.ModelSerializer):
    journey = JourneyTitleSerializer(read_only=True)

    char_class = serializers.CharField(max_length=50, write_only=True)

    class_name = serializers.SerializerMethodField(read_only=True)

    items = ItemGetSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = [
            "id",
            "name",
            "birth_place",
            "race",
            "age",
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
            "level",
            "level_up_points",
            "exp_points",
            "max_exp_points",
            "char_class",
            "class_name",
            "journey",
            "creator_id",
            "items",
        ]
        read_only_fields = [
            "exp_points",
            "max_exp_points",
            "level_up_points",
            "level",
            "items",
        ]

    def create(self, validated_data: dict):
        class_data = validated_data.pop("char_class")
        class_obj, _ = Class.objects.get_or_create(name=class_data)
        return Character.objects.create(**validated_data, class_name=class_obj)

    def get_class_name(self, obj):
        id = obj.__dict__.get("class_name_id")
        classes = Class.objects.get(pk=id)
        return classes.name


class AddRemoveItemToInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"
        read_only_fields = [
            "id",
            "name",
            "birth_place",
            "race",
            "age",
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
            "level",
            "level_up_points",
            "exp_points",
            "max_exp_points",
            "char_class",
            "class_name",
            "journey",
            "creator_id",
            "items",
        ]
