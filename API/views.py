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
# ----------------------------- Users Api View
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UsersApiView(request):
    user = User.objects.all()
    serializer = UsersApi(user, many=True)
    return Response(serializer.data)
# ----------------------------- Users Api View
# ----------------------------- View User
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def SingleUserApi(request, username):
    user = User.objects.get(username=username)
    serializer = UsersApi(user, many=False)
    return Response(serializer.data)
# ----------------------------- View User
# ----------------------------- Creat User via API
@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def CreateUserViaApi(request):
    serializer = UsersApi(data=request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"err": "saqlanmadi. Nimadir xato ketdi"})
# ----------------------------- Creat User via API
# ----------------------------- Update User via API
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def UpdateUserViaApi(request, pk):
    user_data = User.objects.get(id=pk)
    serializer = UsersApi(instance=user_data, data=request.data)
    if serializer.is_valid():
        if request.user.id == user_data.id:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"err": "Siz bu hisob egasi emassiz."})
    else:
        return Response({"err": "saqlanmadi. Nimadir xato ketdi"})
# ----------------------------- Update User via API
# ----------------------------- Users API ----------------------------- #

# ----------------------------- Profile API ----------------------------- #
# ----------------------------- Get Profile data
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def ProfileApiView(request):
    profiles = Profile.objects.all()
    serializer = ProfileApi(profiles, many=True)
    return Response(serializer.data)
# ----------------------------- Get Profile data
# ----------------------------- Single Profile View
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def SingleProfileApiView(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileApi(profile, many=False)
    return Response(serializer.data)
# ----------------------------- Single Profile View
# ----------------------------- Profile API ----------------------------- #

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

# ----------------------------- Chart.Element API ----------------------------- #
# ----------------------------- View Elements

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def ElementApiView(request):
    elem = Element.objects.all()
    serializer = ElementApi(elem, many=True)
    return Response(serializer.data)

# ----------------------------- View Elements
# ----------------------------- Chart.Element API ----------------------------- #

# ----------------------------- ContactUs API ----------------------------- #
# ----------------------------- View Requests
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def ContactUsApiView(request):
    requests = ContactUs.objects.all()
    serializer = ContactUsApi(requests, many=True)
    return Response(serializer.data)
# ----------------------------- View Requests
# ----------------------------- View Request
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def SingleRequestApi(request, pk):
    request_ = ContactUs.objects.get(id=pk)
    serializer = ContactUsApi(request_, many=False)
    return Response(serializer.data)
# ----------------------------- View Request
# ----------------------------- Create Request
@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def CreateRequestViaApi(request):
    serializer = ContactUsApi(data=request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# ----------------------------- Create Request
# ----------------------------- Update Request
@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def UpdateRequestApi(request, pk):
    request_ = ContactUs.objects.get(id=pk)
    serializer = ContactUsApi(instance=request_, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# ----------------------------- Update Request
# ----------------------------- ContactUs API ----------------------------- #

