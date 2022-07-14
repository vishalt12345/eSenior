from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='sender',
        on_delete=models.CASCADE,
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='receiver',
        on_delete=models.CASCADE,
    )
    message = models.TextField(default="")
    time_sent= models.DateTimeField(auto_now_add=True)
    