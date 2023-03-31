from django.shortcuts import render
from First import models
from rest_framework import status, permissions, viewsets, generics
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from First.serializers import UserSerializer

# display all users first way
class UsersDisplay(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

# display alll users using functions
'''
@api_view(['GET','POST'])
def displayUsers(request):
    if request.method == 'GET':
        users = models.CustomUser.objects.all()
        serializer = UserSerializer
        return Response(serializer.data)

'''