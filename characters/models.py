from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class StatusOptions(models.TextChoices):
    HT = ('healthy',)
    DD = ('dead',)


class Character(models.Model):
    name = models.CharField(max_length=50)
    birth_place = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    description = models.TextField(max_length=255)
    health_points = models.IntegerField()
    status = models.CharField(max_length=50, choices=StatusOptions.choices)
    mana_points = models.IntegerField()
    inteligence_points = models.IntegerField()
    strength_points = models.IntegerField()
    stamina_points = models.IntegerField()
    dexterity_points = models.IntegerField()
    attack_points = models.IntegerField()
    defense_points = models.IntegerField()
    exp_points = models.IntegerField()
    max_exp_points = models.IntegerField()
    level_up_points = models.IntegerField()
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    # class_id = models.ForeignKey("classes.Class", on_delete=models.CASCADE, related_name="characters")
    # journey_id = models.ForeignKey("journeys.Journey", on_delete=models.CASCADE, related_name="characters")
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="characters")
