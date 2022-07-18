from django.db import models
import uuid


class System(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    dice = models.IntegerField()
    version = models.FloatField()
    is_active = models.BooleanField(default=True)
    classes = models.ManyToManyField("classes.Class", "systems")
    created_at = models.DateTimeField(auto_now_add=True)
    
