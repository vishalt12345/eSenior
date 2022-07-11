from django.db import models
from django.conf import settings
from datetime import date


# Create your models here.
class Meetings(models.Model):
    senior = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='cgmeetings_senior')
    caregiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='cgmeetings_caregiver')
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(default="")
    recording = models.URLField()
