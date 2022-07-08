from django.db import models
from django.conf import settings

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    caregivers = models.ManyToManyField(settings.AUTH_USER_MODEL)
    def __str__(self):
        return self.name