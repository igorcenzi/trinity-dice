import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import CustomUserManager


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    is_master = models.BooleanField()
    phone = models.CharField(max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active: models.BooleanField(default=True)

    REQUIRED_FIELDS = ["username", "password", "is_master"]
    USERNAME_FIELD = "email"
    objects = CustomUserManager()
