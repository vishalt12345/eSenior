from rest_framework import serializers

from .models import CaregiverProfile

class CgMProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaregiverProfile
        fields = ('user', 'qualifications', 'priceperhour')