"""
    Now we know that serializer work like django Forms
    Using this form of passing information we can create objects
    In ours applications
"""

from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['name', 'surname','city','region',
                  'zip_code','email_address', 'mobile_phone','password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user