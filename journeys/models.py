from django.db import models

class StatusOptions(models.TextChoices):
    CR = ('created',)
    ST = ('start',)
    FS = ('finished',)

class Journey(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    min_level = models.IntegerField()
    max_level = models.IntegerField()
    max_players = models.IntegerField()
    table_link = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=StatusOptions.choices)
    started_at = models.CharField(max_length=255)
    ended_at = models.CharField(max_length=255)
    system_name = models.ForeignKey("systems.System", on_delete=models.CASCADE, related_name="journeys")
    creator_id = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="journeys")

