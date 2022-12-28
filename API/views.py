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
def UsersApi(request):
    user = User.objects.all()
    serializer = UsersApi(user, many=True)
    return Response(serializer.data)

# ----------------------------- Users API ----------------------------- #