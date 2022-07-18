import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class StatusOptions(models.TextChoices):
    HT = ("Healthy",)
    DD = ("Dead",)


class Character(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    birth_place = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    description = models.TextField(max_length=255)
    status = models.CharField(max_length=50, choices=StatusOptions.choices)
    health_points = models.IntegerField()
    mana_points = models.IntegerField()
    intelligence_points = models.IntegerField()
    strength_points = models.IntegerField()
    stamina_points = models.IntegerField()
    dexterity_points = models.IntegerField()
    attack_points = models.IntegerField()
    defense_points = models.IntegerField()
    exp_points = models.IntegerField(default=1)
    max_exp_points = models.IntegerField(default=100)
    level_up_points = models.IntegerField(default=0)
    level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], default=1
    )
    class_name = models.ForeignKey(
        "classes.Class", on_delete=models.CASCADE, related_name="characters"
    )
    journey = models.ForeignKey(
        "journeys.Journey", on_delete=models.CASCADE, related_name="players", null=True
    )
    creator = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="characters"
    )
