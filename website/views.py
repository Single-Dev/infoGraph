from .form import *
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import *


def home(request):
    # Dashboard.objects.get(dahboard=slug)
    # Dashboard.objects.get(id=primkey)
    dashboards = Dashboard.objects.all()
    context={
        "dashboards":dashboards
    }
    return render(request, "pages/home.html", context)

# def test(request, name):
#     dash_name = Dashboard.objects.get(dahboard=name)
#     context={
#         "dash_test":dash_name
#     }
#     return render(request, "test.html", context)



def post_detail(request):
    
    
    dashboards = Dashboard.objects.all()
    context={
        "dashboards":dashboards
    }
    return render(request,' test.html', context)



def new_comment(request, slug, pk):
    Dashboard.objects.get(id=pk)
    template_name = 'com.html'
    post = get_object_or_404(Dashboard, dahboard=slug)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            return redirect('/')
    else:
        comment_form = CommentForm()

    context= {
        'post': post,
        'new_comment': new_comment,
        'comment_form': comment_form
        }
    return render(request, template_name, context)
