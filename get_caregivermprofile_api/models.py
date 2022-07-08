from django.db import models
from django.conf import settings

# Create your models here.
class CaregiverProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    qualifications = models.TextField()
    price = models.DecimalField()
