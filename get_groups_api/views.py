from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import GroupsSerializer
from .models import Groups


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
# Create your views here.
