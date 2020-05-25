from django.shortcuts import render
from django.http import HttpResponse

#dummy blogpost - from db query
posts = [
    {
        'author': 'x',
        'title': 'First Blog',
        'content': 'First Blog Content',
        'date_posted':'25 may 2020'
    },
    {
        'author': 'y',
        'title': 'Second Blog',
        'content': 'Second Blog Content',
        'date_posted':'25 may 2020'
    },
]


# Create your views here.
def blog(request):
    context = {
        'posts' : posts,
        'title' : "Blog test title"
    }
    #render template from defult template directory
    return render(request, 'blogpage/blog.html', context)


def about(request):

    #return response
    return HttpResponse('<h1> Home about </h1>')