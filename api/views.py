from django.shortcuts import render
from First import models
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import APIView
from First.serializers import UserSerializer
class UsersDisplay(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

