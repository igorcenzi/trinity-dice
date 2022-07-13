from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

class TypeOptions(models.TextChoices):
    BUFF = ("B")
    DEBUFF = ("DB")

class Bonus(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    value = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    type = models.CharField(max_length=50, choices=TypeOptions.choices, default=TypeOptions.BUFF)

    