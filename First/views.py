from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import CustomUser

def index(request):
    return render(request, 'index.html')

class UserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
