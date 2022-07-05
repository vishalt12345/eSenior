from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ReminderSerializer
from .models import Reminder


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer