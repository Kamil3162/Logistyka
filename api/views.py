from django.shortcuts import render
from First import models
from rest_framework import status, permissions, viewsets, generics
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from First.serializers import UserSerializer
from TruckOp import models as truckmodels
from TruckOp.serializers import (TruckSerializer,
                                 TruckEqupmentSerializer,
                                 SemiTrailer,
                                 SemiTrailerSerializer)
# display all users first way
class UsersDisplay(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


class SamiTruckDisplay(viewsets.ModelViewSet):
    queryset = truckmodels.Truck.objects.all()
    serializer_class = SemiTrailerSerializer
    #permission_classes = [permissions.IsAuthenticated]

class TruckDisplay(APIView):
    def get(self, request):
        trucks = truckmodels.Truck.objects.all()
        serializer = TruckSerializer(trucks, many=True)
        return Response(serializer.data)


# display alll users using functions
'''
@api_view(['GET','POST'])
def displayUsers(request):
    if request.method == 'GET':
        users = models.CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
'''
