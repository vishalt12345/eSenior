# serializers.py

from rest_framework import serializers

from .models import Groups

class GroupsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Groups
        fields = ('name', 'members')