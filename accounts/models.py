from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    department = models.CharField(max_length=50, blank=True)
    program = models.CharField(max_length=50, blank=True)
    user_id = models.PositiveIntegerField(unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    is_staff = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    def get_full_name(self):
        if self.is_doctor:
            return 'Dr. {}'.format(self.full_name)
        else:
            return self.full_name

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        if self.is_doctor:
            return "Dr. {}".format(self.full_name)
        else:
            return self.full_name