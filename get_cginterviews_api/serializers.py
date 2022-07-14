# myapi/urls.py
# serializers.py

from rest_framework import serializers

from .models import Interviews

class CgInterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviews
        fields = ('senior', 'caregiver', 'timestamp', 'notes', 'recording')