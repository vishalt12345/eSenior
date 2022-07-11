from django.db import models
from django.conf import settings
from datetime import date
# Create your models here.
class Click(models.Model):
    caregiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='analytics_caregiver')
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Analytics_UserClick")
    LastTimeClicked = models.DateTimeField(auto_now_add=True)