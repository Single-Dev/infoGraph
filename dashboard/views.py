from django.shortcuts import render
from .models import Lyrics
from .serializers import LyricsAPI
#rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


def home(request):
    return render (request, 'pages/home.html')

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def LyricsApiView(request):
    krasovka = Lyrics.objects.all()
    serializer = LyricsAPI(krasovka, many=True) 
    return Response(serializer.data)