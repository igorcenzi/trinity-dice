from django.db import models
import uuid

class Journey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    min_level = models.IntegerField()
    max_level = models.IntegerField()
    max_players = models.IntegerField()
    table_link = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default="created")
    started_at = models.CharField(max_length=255, null=True)
    ended_at = models.CharField(max_length=255, null=True)
    system = models.ForeignKey("systems.System", on_delete=models.CASCADE, related_name="journeys")
    creator = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="journeys")

