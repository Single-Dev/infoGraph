from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *



def home(request):
    return render(request, 'pages/home.html')


def AddElementView(request, slug):
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
            return redirect("/")
    else:
        comment_form = AddElementForm()

    context= {
        # 'new_comment': new_comment,
        'comments': comments,
        'comment_form': comment_form,
        "dashboard":dashboard
        }
    
    return render(request, "pages/dashboard.html", context)