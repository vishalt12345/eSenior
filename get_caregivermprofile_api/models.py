from django.db import models
from django.conf import settings

# Create your models here.
class CaregiverProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='caregivermprofile_user')
    qualifications = models.TextField(default="")
    priceperhour = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
