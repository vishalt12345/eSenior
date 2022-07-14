from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ContactsSerializer
from .models import Contact


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer
    def perform_create(self, serializer, **kwargs):
        kwargs['user'] = self.request.user
        serializer.save(user=self.request.user)
# Create your views here.