from django.shortcuts import render
from API.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, filters, generics
from django.contrib.auth import get_user_model
User = get_user_model()


def home(request):
    return render(request, 'pages/home.html')

# ----------------------------- Users API ----------------------------- #
# ----------------------------- View User
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def SingleUserApi(request, username):
    user = User.objects.get(username=username)
    serializer = UsersApi(user, many=False)
    return Response(serializer.data)
# ----------------------------- View User
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
# ----------------------------- Search Users via API
class UserSearchViaApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersApi
    filter_backends = [filters.SearchFilter]
    search_fields = ["username", "email", "first_name"]
# ----------------------------- Search Users via API
# ----------------------------- Users API ----------------------------- #

# ----------------------------- Profile API ----------------------------- #
# ----------------------------- Get Profile data
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def ProfilesApiView(request):
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
# ----------------------------- View Chart
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def SingleChartApi(request, slug):
    chart = Chart.objects.get(slug=slug)
    serializer = ChartAPi(chart, many=False)
    return Response(serializer.data)

# ----------------------------- View Chart
# ----------------------------- Search Chart
class ChartSearchViaApiView(generics.ListAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartAPi
    filter_backends = [filters.SearchFilter]
    search_fields = ["slug", "name",]
# ----------------------------- Search Chart
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

