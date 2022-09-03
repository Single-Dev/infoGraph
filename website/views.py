from urllib import request
from django.shortcuts import render
from django.views import generic
from .models import *

class Home(generic.TemplateView):
    template_name = "pages/home.html"

def test(request, name):
    dash_name = Dashboard.objects.get(dahboard=name)
    dash_all = Dashboard.objects.all()
    context={
        "dash_test":dash_name,
        "dash_all":dash_all
    }
    return render(request, "test.html", context)