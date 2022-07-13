from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
