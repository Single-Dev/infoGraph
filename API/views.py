from django.shortcuts import render
from API.serializers import *
from django.contrib.auth import get_user_model
User = get_user_model()

#rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, filters, generics


def home(request):
    return render(request, 'pages/home.html')

# ----------------------------- Users API ----------------------------- #

# users get data
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UsersApiView(request):
    user = User.objects.all()
    serializer = UsersApi(user, many=True)
    return Response(serializer.data)

# View User
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def SingleUserApi(request, username):
    user = User.objects.get(username=username)
    serializer = UsersApi(user, many=False)
    return Response(serializer.data)

# Creat User via API
@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def CreateUserViaApi(request):
    serializer = UsersApi(data=request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Update User via API
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def UpdateUserViaApi(request, pk):
    user_data = User.objects.get(id=pk)
    serializer = UsersApi(instance=user_data, data=request.data)
    if serializer.is_valid():
        if request.user.id == user_data.id:
            serializer.save()
    return Response(serializer.data)


# ----------------------------- Users API ----------------------------- #
# ----------------------------- Charts API ----------------------------- #
# ----------------------------- Get Charts
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def ChartApiView(request):
    chart = Chart.objects.all()
    serializer = ChartAPi(chart, many=True)
    return Response(serializer.data)
# ----------------------------- Get Charts

# ----------------------------- View Chart
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def SingleChartApi(request, slug):
    chart = Chart.objects.get(slug=slug)
    serializer = ChartAPi(chart, many=False)
    return Response(serializer.data)

# ----------------------------- View Chart

# ----------------------------- Charts API ----------------------------- #
