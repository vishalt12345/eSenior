from django.db import models
from datetime import date
from django.conf import settings
# Create your models here.
class Reminder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reminders_user')
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default="")

    def __str__(self):
        return self.name