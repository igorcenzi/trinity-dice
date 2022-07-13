from django.db import models


class ItemType(models.TextChoices):
    WEAPON = ("WP", "Weapon")
    ARMOR = ("AM", "Armor")
    ARTIFACT = ("AR", "Artifact")

class ItemRarity(models.TextChoices):
    COMMON = ("CM", "Common")
    UNCOMMON = ("UC", "Uncommon")
    RARE = ("RR", "Rare")

class Item(models.Model):
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
        'systems.System', on_delete=models.CASCADE, related_name='system'
    )
    characters = models.ManyToManyField(
       'characters.Character', related_name='character'
    )
    classes = models.ManyToManyField(
       'classes.Class', related_name='classes'
    )
    """

