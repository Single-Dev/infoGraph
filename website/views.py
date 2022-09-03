from .form import *
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *

class Home(generic.TemplateView):
    template_name = "pages/home.html"

# def test(request, name):
#     dash_name = Dashboard.objects.get(dahboard=name)
#     context={
#         "dash_test":dash_name
#     }
#     return render(request, "test.html", context)



def post_detail(request, slug):
    template_name = 'test.html'
    post = get_object_or_404(Dashboard, dahboard=slug)
    comments = post.comments.filter(active=True)
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
    else:
        comment_form = CommentForm()

    context= {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form}
    return render(request, template_name, context)


def new_coment(request, pk):
    template_name = 'test.html'
    post = get_object_or_404(Dashboard, dahboard=pk)
    comments = post.comments.filter(active=True)
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
    else:
        comment_form = CommentForm()

    context= {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form}
    return render(request, template_name, context)
