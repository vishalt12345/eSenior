from django.db import models
from django.conf import settings

# Create your models here.
class Groups(models.Model):
     name = models.CharField(max_length=300, default="Untitled Group");
     members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='groups_members')
     def __str__(self):
        return self.name


