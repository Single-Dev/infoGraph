from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth import get_user_model

User = get_user_model()



def home(request):
    dashboard = Dashboard.objects.all()
    dashboard_form = DashboardForm()
    initial = {'key': 'value'}
    if request.method == "POST":
        dashboard_form = DashboardForm(request.POST)
        if dashboard_form.is_valid():
            dashboard_form.save()
            slug = dashboard_form.cleaned_data.get('slug')
            dashboard_form.save()
            return redirect('app:stats', slug)
    context={
        "dash":dashboard,
        "dashboard_form":dashboard_form
    }
    return render(request, 'pages/home.html', context)

def PublicProfileView(request, username):
    tab = request.GET.get('tab')
    if tab == "charts":
        user_dashboards = Dashboard.objects.all()
    else:
        user_dashboards = ""
    user_profile = User.objects.get(username=username)
    context = {
        "user_profile": user_profile,
        "user_dashboards":user_dashboards
    }
    return render(request, 'pages/profile.html', context)

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