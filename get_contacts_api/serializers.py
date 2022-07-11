# serializers.py

from rest_framework import serializers

from .models import Contact

class ContactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('user', 'contacts')