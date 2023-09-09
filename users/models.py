from django.db import models
from django.contrib.auth.models import AbstractUser


class SystemUser(AbstractUser):
    USERNAME_FIELD = "email"
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField("email address", unique=True)

    REQUIRED_FIELDS = []
