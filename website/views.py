from urllib import request
from django.shortcuts import render
from django.views import generic
from .models import *

class Home(generic.TemplateView):
    template_name = "pages/home.html"

def test(request, name):
    dash_name = Dashboard.objects.get(dahboard=name)
    context={
        "dash_test":dash_name
    }
    return render(request, "test.html", context)