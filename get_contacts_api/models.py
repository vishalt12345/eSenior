from django.db import models
from django.conf import settings
# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='contact_user', default=None)
    contacts = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='contact_contacts')
    def __str__(self):
        return self.name

