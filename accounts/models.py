from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    department = models.CharField(max_length=50, blank=True)
    program = models.CharField(max_length=50, blank=True)
    user_id = models.PositiveIntegerField(unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, blank=True)
    is_staff = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)
