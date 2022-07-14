from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import CgMProfileSerializer
from .models import CaregiverProfile


class CgMProfileViewSet(viewsets.ModelViewSet):
    queryset = CaregiverProfile.objects.all()
    serializer_class = CgMProfileSerializer
    def perform_create(self, serializer, **kwargs):
        kwargs['user'] = self.request.user
        serializer.save(user=self.request.user)