from django.db import models
import uuid


class ItemType(models.TextChoices):
    WEAPON = ("Weapon")
    ARMOR = ("Armor")
    ARTIFACT = ("Artifact")

class ItemRarity(models.TextChoices):
    COMMON = ("Common")
    UNCOMMON = ("Uncommon")
    RARE = ("Rare")

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(
        max_length=50,
        choices=ItemType.choices,
        default=ItemType.WEAPON
    )
    rarity = models.CharField(
        max_length=50,
        choices=ItemRarity.choices,
        default=ItemRarity.COMMON
    )
    precision = models.IntegerField()
    min_level = models.IntegerField()

    """
    original_system = models.ForeignKey(
        'systems.System', on_delete=models.CASCADE, related_name='items'
    )
    characters = models.ManyToManyField(
       'characters.Character', related_name='inventories'
    )
    classes = models.ManyToManyField(
       'classes.Class', related_name='items'
    )
    bonus = models.ManyToManyField(
       'bonus.Bonus', related_name='items'
    )
    """

