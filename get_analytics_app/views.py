from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import AnalyticsSerializer
from .models import Click


class AnalyticsViewSet(viewsets.ModelViewSet):
    queryset = Click.objects.all()
    serializer_class = AnalyticsSerializer

# Create your views here.
