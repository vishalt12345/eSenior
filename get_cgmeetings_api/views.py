from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import CgMeetingsSerializer
from .models import Meetings


class CgMeetingsViewSet(viewsets.ModelViewSet):
    queryset = Meetings.objects.all()
    serializer_class = CgMeetingsSerializer
