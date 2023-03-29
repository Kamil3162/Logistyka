"""
    Now we know that serializer work like django Forms
    Using this form of passing information we can create objects
    In ours applications
"""

from .models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'email_address']
