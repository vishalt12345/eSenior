from django.db import models
from django.conf import settings
# Create your models here.
class Contact(models.Model):
    firstcontact = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    secondcontact = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    def __str__(self):
        return self.name

