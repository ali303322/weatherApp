# models.py

from django.db import models

class Activity(models.Model):
    activity = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='activities/')  # Store images in media/activities/

    def __str__(self):
        return self.activity
