from django.shortcuts import render
from API.serializers import *
from django.contrib.auth import get_user_model
User = get_user_model()

#rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, filters, generics


# ----------------------------- Users API ----------------------------- #

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UsersApiView(request):
    user = User.objects.all()
    serializer = UsersApi(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def CreateUserViaApi(request):
    serializer = UsersApi(data=request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def UpdateUserViaApi(request, pk):
    user_data = User.objects.get(id=pk)
    serializer = UsersApi(instance=user_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# ----------------------------- Users API ----------------------------- #