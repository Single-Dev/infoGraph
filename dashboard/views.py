from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *



def home(request):
    return render(request, 'pages/home.html')


def AddElementView(request, slug):
    template_name = 'pages/add.html'
    post = get_object_or_404(Dashboard, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = AddElementForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = AddElementForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})