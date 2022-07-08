from django.db import models
from django.conf import settings
# Create your models here.
class Interviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    caregiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    timestamp = models.DateTimeField()
    recording = models.URLField()