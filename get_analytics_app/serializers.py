from rest_framework import serializers

from .models import Click

class AnalyticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Click
        fields = ('caregiver', 'user', 'LastTimeClicked')