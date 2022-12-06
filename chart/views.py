from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from django.db.models import Avg
from django.urls import reverse 
from django.db.models import Q
from .models import *
from .forms import *
User = get_user_model()


def home(request):
    charts_count = Chart.objects.count()
    user_count = User.objects.count()
    date_joined_count = User.objects.filter(date_joined__date=timezone.now()-timezone.timedelta(0)).count()
    users = User.objects.all().order_by('-id')[:date_joined_count]
    elem_count = Element.objects.count()
    following_actions = None
    # created_on_count = None
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=request.user)
        # for user_f in user.followers.all():
        #     created_on_count = user_f.chart.filter(created_on__date=timezone.now()).count()
        following_actions = user.followers.all().order_by('-id')[:15]

    contact = ContactUsForm()
    if request.method == "POST":
        contact = ContactUsForm(request.POST)
        if contact.is_valid():
            contact.save()
            return redirect('app:home')
    context = {
        "charts_count":charts_count,
        "user_count":user_count,
        "elem_count":elem_count,
        "following_actions":following_actions,
        "users":users,
        "contact":contact
    }
    return render(request, 'pages/home.html', context)

def signup(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
    
    return render(request, 'registration/signup.html', {"form":form})

def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("app:home")
            else:
                messages.error(request,"Invalid username or password.")
    else:
        # messages.error(request,"Invalid username or password.")
        form = AuthenticationForm()

    context={
        "form":form
    }
    return render(request, "registration/login.html", context)

def logoutView(request):
    logout(request)
    return redirect("app:home")

@login_required(login_url='/login/')
def deleteUser(request):
    user = User.objects.get(username=request.user)
    user.delete()
    return redirect("/")

def ProfileView(request, username):
        user_p = User.objects.get(username=username)
        author = get_object_or_404(User, username=username)
        # Tab
        tab = request.GET.get('tab')
        title = None
        tab_chart = None
        tab_following = None
        tab_followers = None
        if tab == "charts":
            tab_chart = author.chart.all()
            title = "Charts"
        elif tab == "following": # followingda foydalanuvchi uchun followerslar keladi. followersda esa teskarisi
            tab_followers = user_p.followers.all()
            title = "Following"

        elif tab == "followers":
            title = "Followers"
            tab_following = user_p.following.all()
        else:
            title = f"Charts - @{user_p.username}"

        # Epdate Profile
        if request.user.is_authenticated:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileForm(instance=request.user.profile)
            if request.method == 'POST':
                user_form = UpdateUserForm(request.POST, instance=request.user)
                profile_form = UpdateProfileForm(request.POST,
                                                request.FILES,
                                                instance=request.user.profile)
                if user_form.is_valid() and profile_form.is_valid():
                    user_name = user_form.cleaned_data.get('username')
                    user_form.save()
                    profile_form.save()
                    return redirect("app:profile", user_name)
                
        else:
            user_form = None
            profile_form = None

        user_chart_count = author.chart.count()

        # Pagination
        chart_list = Chart.objects.all()
        paginator = Paginator(chart_list, 1) # Show 1 contacts per page.
        page_number = request.GET.get('tab=chart')
        page_obj = paginator.get_page(page_number)
        # Pagination

        context = {
            "user_p": user_p,
            "user_following":tab_following,
            "user_followers":tab_followers,
            "user_form":user_form,
            "profile_form":profile_form,
            "tab_chart":tab_chart,
            "title":title,
            "user_chart_count":user_chart_count,
            "page_obj":page_obj
        }
        return render(request, 'pages/profile.html', context)

def followToggle(request, author):
    if request.user.is_authenticated:
        authorObj = User.objects.get(username=author)
        currentUserObj = User.objects.get(username=request.user.username)
        following = authorObj.following.all()

        if author != currentUserObj.username:
            if currentUserObj in following:
                authorObj.following.remove(currentUserObj.id)
            else:
                authorObj.following.add(currentUserObj.id)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("app:login")

def password_change(request):
    if request.user.is_authenticated:
        form  = PasswordChangeForm(user=request.user, data=request.POST)
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect("app:profile", request.user.username)
        context={
            "form":form,
        }
        return render(request, "pages/settings/password_change.html", context )
    else:
        return redirect(f'app:login')

@login_required(login_url='/login/')
def settings(request):
    return render(request, "pages/settings/settings.html")

@login_required(login_url='/login/')
def NewChartView(request):
    user_p = User.objects.get(username=request.user)
    user = User.objects.get(username=request.user)
    author = get_object_or_404(User, username=request.user)
    dash = author.chart.all()
    new_dash = None
    NewChart = ChartFrom()
    if request.method == 'POST':
        NewChart = ChartFrom(data=request.POST)
        if NewChart.is_valid():
            new_dash = NewChart.save(commit=False)
            slug = NewChart.cleaned_data.get('slug')
            new_dash.author = author
            new_dash.save()
            return redirect("app:chart", slug) 
   
    context={
        "NewChart":NewChart,
    }
    return render(request, "pages/new.html", context)

def ChartView(request, slug):
    chart = Chart.objects.get(slug=slug)
    post = get_object_or_404(Chart, slug=slug)
    elements = post.element.all()
    elements_count = post.element.count()
    number_avg = post.element.aggregate(Avg("value"))
    new_element= None
    # add element form
    if request.method == 'POST':
        comment_form = ElementForm(data=request.POST)
        if comment_form.is_valid():
            new_element = comment_form.save(commit=False)
            new_element.post = post
            new_element.save()
            return redirect("app:chart", slug) # redirect to this url
    else:
        comment_form = ElementForm()
    context= {
        'elements': elements,
        'comment_form': comment_form,
        "chart":chart,
        "elements_count":elements_count,
        "number_avg":number_avg,
        }
    
    return render(request, "pages/chart.html", context)

def UpdateChartView(request, slug):
    chart = Chart.objects.get(slug=slug)
    post = get_object_or_404(Chart, slug=slug)
    elements = post.element.all()
    update_chart_form = ChartFrom(instance=chart)
    if request.method == 'POST':
        update_chart_form = ChartFrom(request.POST, instance=chart)
        if update_chart_form.is_valid():
            update_chart_form.save()
            slug = update_chart_form.cleaned_data.get('slug')
            return redirect("app:chart", slug)
    context={
        "update_chart_form":update_chart_form,
        "chart":chart,
        "elements":elements
    }
    return render(request, "pages/update_chart.html", context)

def deleteChartView(request, slug):
    chart = Chart.objects.get(slug=slug)
    if request.user.username == chart.author.username: 
        chart.delete()
        return redirect("app:profile", chart.author) # yoki request.user
    else:
        slug = chart.slug
        return redirect("app:chart", slug)

def UpdateElementView(request, slug, pk):
    chart = Chart.objects.get(slug=slug)
    post = get_object_or_404(Chart, slug=slug)
    element = post.element.get(id=pk)
    UpdateElementForm = ElementForm(instance=element)
    if chart.author.username == request.user.username:
        if request.method == "POST":
            UpdateElementForm = ElementForm(request.POST, instance=element)
            if UpdateElementForm.is_valid():
                UpdateElementForm.save()
                return redirect("app:update_chart", chart.slug)
    else:
        return render(request, "pages/helpers/404.html")
    context={
        "UpdateElementForm":UpdateElementForm,
        "element":element,
        "chart":chart
    }
    return render(request, "pages/edit_element.html", context)

def deleteElementView(request, slug, pk):
    chart = Chart.objects.get(slug=slug)
    post = get_object_or_404(Chart, slug=slug)
    element = post.element.get(id=pk)
    if request.user.username == chart.author.username: 
        element.delete()
        return redirect("app:update_chart", chart.slug)
    else:
        return render("app:chart", chart.slug)

def handler404(request, exception):
    return render(request, "pages/helpers/404.html")

def handler500(request, *args, **argv):
    return render(request, 'pages/helpers/404.html')

def results(request):
    search = None
    users = None
    charts = None
    user_count = 0
    chart_count = 0
    if 'q' in request.GET:
        search = request.GET['q']
        user_search = Q(Q(username__icontains=search))
        chart_search = Q(Q(slug__icontains=search))
        users = User.objects.filter(user_search)
        charts = Chart.objects.filter(chart_search)
        user_count = users.count()
        chart_count = charts.count()
    if len(search) < 3: # bitta harf bilan qidirmaslig uchun
        return redirect('app:home')
    context={
        "users":users,
        "charts":charts,
        "user_count":user_count,
        "chart_count":chart_count,
        "search":search
    }
    return render(request, "pages/result.html", context)

@login_required(login_url='login')
def VerifyRequestView(request):
    form = AccountVerifyForm()
    if request.method == "POST":
        form = AccountVerifyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:profile', request.user.username)
    
    context={
        "form":form
    }
    return render(request, "pages/settings/verify_request.html", context)