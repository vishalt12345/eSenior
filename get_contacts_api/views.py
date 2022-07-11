from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ContactsSerializer
from .models import Contact


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer
# Create your views here.