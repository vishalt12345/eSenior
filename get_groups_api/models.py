from django.db import models
from django.conf import settings

# Create your models here.
class Groups(models.Model):
     name = models.CharField(max_length=300);
     members = models.ManyToManyField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
     def __str__(self):
        return self.name


