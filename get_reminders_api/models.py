from django.db import models
from datetime import date
# Create your models here.
class Reminder(models.Model):
    date = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return self.name