from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models

from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_events')
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='events_attended')

    def __str__(self):
        return self.title

    created_at = models.DateTimeField(default=timezone.now)
