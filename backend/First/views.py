from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import (login,
                                 logout,
                                 authenticate,
                                 get_user_model)
from rest_framework import permissions
def index(request):
    return render(request, 'index.html')

# we will generate a profil to create a user
class CreateUserAPI(APIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def post(self, request):
        print('this is post method to add data to api ')
        print(request.data.get('name'))
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()        # we save this is our database
            user.name = user.name.title()
            user.surname = user.surname.title()
            user.save()
            return Response(status=status.HTTP_201_CREATED, data={'code':'esa'})
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, data=serializer.errors)

    def get(self, request):
        print('This is get method to display data in api ')
        users = CustomUser.objects.all()
        data = UserSerializer(users,many=True).data
        return Response(data, status=status.HTTP_200_OK)

class LogoutUserAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.get(pk=kwargs['pk'])
            logout(user)
            return Response(status=status.HTTP_200_OK)
        except user.DoesNotExist:
            raise ValueError("following object does not exist")
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error':'User not found'})

class LoginUserAPI(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        if request.data:
            print(request.data)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)