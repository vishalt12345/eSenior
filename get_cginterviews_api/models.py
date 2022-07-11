from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.
class Interviews(models.Model):
    senior = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='cginterviews_senior')
    caregiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='cginterviews_caregiver')
    timestamp = models.DateTimeField()
    notes = models.TextField(default="")
    recording = models.URLField()