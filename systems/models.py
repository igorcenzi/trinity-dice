from django.db import models


class System(models.Model):
    name = models.CharField(max_length=50)
    dice = models.IntegerField()
    version = models.DecimalField(max_digits=16, decimal_places=2)
    is_active = models.BooleanField(default=True)
    classes = models.ManyToManyField("classes.Class", "systems")
