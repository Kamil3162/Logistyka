"""
    Now we know that serializer work like django Forms
    Using this form of passing information we can create objects
    In ours applications
"""

from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['name', 'surname','city','region',
                  'zip_code', 'email_address', 'mobile_phone','password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(username=clean_data.get('email'),
                            password=clean_data.get('password'))
        if user:
            return user
        raise ValidationError('user not found')