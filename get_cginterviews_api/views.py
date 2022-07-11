from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import CgInterviewSerializer
from .models import Interviews


class CgInterviewsViewSet(viewsets.ModelViewSet):
    queryset = Interviews.objects.all()
    serializer_class = CgInterviewSerializer

# Create your views here.
