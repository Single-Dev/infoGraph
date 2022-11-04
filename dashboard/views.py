from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import *
from .forms import *

User = get_user_model()



def home(request):
    dashboards_count = Dashboard.objects.count()
    user_count = User.objects.count()
    elem_count = Element.objects.count()
    context = {
        "dashboards_count":dashboards_count,
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
        tab_dashboards = author.tanla.all()
        title = "Charts"
    else:
        tab_dashboards = ""
        title = f"amCharts - @{user_p.username}"

    dash_count = author.tanla.count()
    context = {
        "user_p": user_p,
        "dashboard":tab_dashboards,
        "title":title,
        "dash_count":dash_count
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
        addDashForm = DashboardForm(data=request.POST)
        if addDashForm.is_valid():
            new_dash = addDashForm.save(commit=False)
            slug = addDashForm.cleaned_data.get('slug')
            messages.success(request, f'{slug}')
            new_dash.author = author
            new_dash.save()
            return redirect("app:stats", slug) 
    else:
        addDashForm = DashboardForm()
    context={
        "user_p": user_p,
        "addDashForm":addDashForm,
    }
    return render(request, "pages/new.html", context)

def signup(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request, 'registration/signup.html', {"form":form})

def StatsView(request, slug):
    dashboard = Dashboard.objects.get(slug=slug)
    post = get_object_or_404(Dashboard, slug=slug)
    comments = post.qoshish.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = AddElementForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect("app:stats", slug) # redirect to this url
    else:
        comment_form = AddElementForm()

    context= {
        # 'new_comment': new_comment,
        'comments': comments,
        'comment_form': comment_form,
        "dashboard":dashboard
        }
    
    return render(request, "pages/dashboard.html", context)