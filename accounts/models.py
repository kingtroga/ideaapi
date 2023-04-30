from django.contrib.auth.models import AbstractUser
from django.db import models
import random

SECURITY_QUESTIONS_CHOICES = (
    ('what is your favorite color?', 'What is your favorite color?'),
    ('what is your mother\'s maiden name?', 'What is your mother\'s maiden name?'),
    ('what is the name of your first pet?', 'What is the name of your first pet?'),
)

class CustomUser(AbstractUser):
    department = models.CharField(max_length=50, blank=True)
    program = models.CharField(max_length=50, blank=True)
    user_id = models.PositiveIntegerField(unique=True, blank=True, primary_key=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    is_staff = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    security_question = models.CharField(max_length=255, choices=SECURITY_QUESTIONS_CHOICES)
    secureQusAns = models.CharField(max_length=255)

    def check_answer(self, secureQusAns):
        return self.secureQusAns == secureQusAns

    def get_full_name(self):
        if self.is_doctor:
            return 'Dr. {}'.format(self.full_name)
        else:
            return self.full_name

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self.generate_user_id()
        super().save(*args, **kwargs)
    
    def generate_user_id(self):
        # generate a random 13 digit integer
        return str(random.randint(10**12, 10**13-1))


    def __str__(self):
        if self.is_doctor:
            return "Dr. {}".format(self.full_name)
        else:
            return self.full_name