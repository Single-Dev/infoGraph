from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import *
from .forms import *

User = get_user_model()


def home(request):
    charts_count = Chart.objects.count()
    user_count = User.objects.count()
    elem_count = Element.objects.count()
    context = {
        "charts_count":charts_count,
        "user_count":user_count,
        "elem_count":elem_count
    }
    return render(request, 'pages/home.html', context)

def PublicProfileView(request, username):
    user_p = User.objects.get(username=username)
    author = get_object_or_404(User, username=username)
    # Tab
    tab = request.GET.get('tab')
    title = None
    if tab == "charts":
        tab_chart = author.tanla.all()
        title = "Charts"
    else:
        tab_chart = ""
        title = f"amCharts - @{user_p.username}"

    user_chart_count = author.tanla.count()
    context = {
        "user_p": user_p,
        "tab_chart":tab_chart,
        "title":title,
        "user_chart_count":user_chart_count
    }
    return render(request, 'pages/profile.html', context)

def NewDashboardView(request, username):
    user_p = User.objects.get(username=username)
    initial = {'key': 'value'}
    user = User.objects.get(username=username)
    author = get_object_or_404(User, username=username)
    dash = author.tanla.filter(active=True)
    new_dash = None
    if request.method == 'POST':
        NewChart = NewChartFrom(data=request.POST)
        if NewChart.is_valid():
            new_dash = NewChart.save(commit=False)
            slug = NewChart.cleaned_data.get('slug')
            new_dash.author = author
            new_dash.save()
            return redirect("app:chart", slug) 
    else:
        NewChart = NewChartFrom()
    context={
        "user_p": user_p,
        "NewChart":NewChart,
    }
    return render(request, "pages/new.html", context)

def signup(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, 'registration/signup.html', {"form":form})

def StatsView(request, slug):
    dashboard = Chart.objects.get(slug=slug)
    post = get_object_or_404(Chart, slug=slug)
    comments = post.qoshish.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = NewElementForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect("app:chart", slug) # redirect to this url
    else:
        comment_form = NewElementForm()

    context= {
        'comments': comments,
        'comment_form': comment_form,
        "dashboard":dashboard
        }
    
    return render(request, "pages/dashboard.html", context)