from django.db import models
from django.conf import settings

# Create your models here.
class Message(models.Model):

    """
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='sender',
        on_delete=models.CASCADE,
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='receiver',
        on_delete=models.CASCADE,
    )
    """
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    message = models.TextField()
    time_sent= models.TimeField(auto_now_add=True)