from django.conf import settings
from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title