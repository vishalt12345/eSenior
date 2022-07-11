from django.db import models
from django.conf import settings

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='caregivercart_user')
    caregivers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='caregivercart_caregivers')
    def __str__(self):
        return self.name