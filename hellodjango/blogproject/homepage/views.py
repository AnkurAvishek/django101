from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def home(request):

    #render template from defult template directory
    return render(request, 'homepage/home.html')


def about(request):
    return render(request, 'homepage/home.html')
