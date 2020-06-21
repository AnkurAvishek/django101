# djanogo101

#virtul environment

#Install django
pip3 install django
python3 -m django --version

#create new project
django-admin startproject django_project

#project structure
-django_porject
    - django_project 
        - __init__.py
        - setting.py
        - urls.py
        - wsgi.py
    -manage.py

setting.py - security key, settings etc.
urls.py - url mapping where to send user
wsgi.py - python web application and webserver communication

#run server
python3 manage.py runserver
#access at http://127.0.0.1:8000

#add apps
python3 manage.py startapp blog

#project

- blog
  - __int__.py
  - admin.py
  - apps.py
  - migrations
     - __init__.py
  - models.py
  - tests.py
  - views.py
-db.sqlite3

# create view
blog$vi views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Blog Home </h1>')

# Create Blog URL module
blog$vi urls.py

from django.urls import path
form . import views

urlpatterns = [
    path('/', views.home, name='blog-home')
]

# Map this url to project urls.
django_project$ vi urls.py

from django.contrib import admin
from dajngo.urls import path, include

urlpatterns [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]

# check
python3 manage.py runserver
curl localhost:8000/blog/

