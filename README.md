# djanogo - blog Application
* Templates and passing variables- dummy data 
* Reduce repeated code in templates - template inheritance
* Add bootstrap; static css
* creating admin page 

# virtul environment

# Install django

---
pip3 install django
python3 -m django --version
---

## create new project
---
django-admin startproject django_project
---

### project structure
-django_porject
    - django_project 
        - __init__.py
        - setting.py
        - urls.py
        - wsgi.py
    -manage.py

* setting.py - security key, settings etc.
* urls.py - url mapping where to send user
* wsgi.py - python web application and webserver communication

## run server

---
python3 manage.py runserver
---

* access at http://127.0.0.1:8000

## Add apps
---
python3 manage.py startapp blog
---

## Create Templates Diretory
---
blog$ mkdir templates
blog$ mkdir templates/blog
blog$ touch templates/blog/home.html
blog$ touch templates/blog/about.html
---
---
- blog
  - __int__.py
  - templates
    - blog
        - home.html
        - about.html
  - admin.py
  - apps.py
  - migrations
     - __init__.py
  - models.py
  - tests.py
  - views.py
-db.sqlite3
---



## add static css files
---
blog$ mkdir static
blog$ mkdir static/blog
blog$ touch static/blog/main.css
blog$ vi static/blog/main.css
---
---
body {
  background: #fafafa;
  color: #333333;
  margin-top: 5rem;
}

h1, h2, h3, h4, h5, h6 {
  color: #444444;
}

ul {
  margin: 0;
}

.bg-steel {
  background-color: #5f788a;
}

.site-header .navbar-nav .nav-link {
  color: #cbd5db;
}

.site-header .navbar-nav .nav-link:hover {
  color: #ffffff;
}

.site-header .navbar-nav .nav-link.active {
  font-weight: 500;
}

.content-section {
  background: #ffffff;
  padding: 10px 20px;
  border: 1px solid #dddddd;
  border-radius: 3px;
  margin-bottom: 20px;
}

.article-title {
  color: #444444;
}

a.article-title:hover {
  color: #428bca;
  text-decoration: none;
}

.article-content {
  white-space: pre-line;
}

.article-img {
  height: 65px;
  width: 65px;
  margin-right: 16px;
}

.article-metadata {
  padding-bottom: 1px;
  margin-bottom: 4px;
  border-bottom: 1px solid #e3e3e3
}

.article-metadata a:hover {
  color: #333;
  text-decoration: none;
}

.article-svg {
  width: 25px;
  height: 25px;
  vertical-align: middle;
}

.account-img {
  height: 125px;
  width: 125px;
  margin-right: 20px;
  margin-bottom: 16px;
}

.account-heading {
  font-size: 2.5rem;
}
---

## make blog template
* Dajango user similar to jinga 2 templenting engine
---
vi blog/templates/blog/base.html
---
---
<!--- generate absoulte url of the static file -->
{% load static %}

<!DOCTYPE html>
<html>
<head>

    <!--- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <!--- load staic file --->
    <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">

    {% if title %}
        <title>Django Blog - {{ title }}</title>
    {% else %}
        <title>Django Blog</title>
    {% endif %}
</head>
<body>
    <header class="site-header">
      <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
        <div class="container">
          <a class="navbar-brand mr-4" href="{% url 'blog-home' %}">Django Blog</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarToggle">
            <div class="navbar-nav mr-auto">
              <a class="nav-item nav-link" href="{% url 'blog-home' %}">Home</a>
              <a class="nav-item nav-link" href="{% url 'blog-about' %}">About</a>
            </div>
            <!-- Navbar Right Side -->
            <div class="navbar-nav">
              {% if user.is_authenticated %}
                <a class="nav-item nav-link" href="{% url 'Profile' %}">Profile</a>
                <a class="nav-item nav-link" href="{% url 'logout' %}">Logout</a>
              {% else %}
                <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
                <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
              {% endif %}
            </div>
          </div>
        </div>
      </nav>
    </header>
    <main role="main" class="container">
      <div class="row">
        <div class="col-md-8">
          {% if messages %}
              {% for message in messages %}
                  <div class="alert alert-{{ message.tags}}">
                  {{ message }}
                  </div>
              {% endfor %}
          {% endif %}
          {% block content %}{% endblock %}
        </div>
        <div class="col-md-4">
          <div class="content-section">
            <h3>Our Sidebar</h3>
            <p class='text-muted'>You can put any information here you'd like.
              <ul class="list-group">
                <li class="list-group-item list-group-item-light">Latest Posts</li>
                <li class="list-group-item list-group-item-light">Announcements</li>
                <li class="list-group-item list-group-item-light">Calendars</li>
                <li class="list-group-item list-group-item-light">etc</li>
              </ul>
            </p>
          </div>
        </div>
      </div>
    </main>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  
</body>
</html>
---

## overide content block
---
vi blog/templates/blog/home.html
---
---
{% extends "blog/base.html" %}
    {% block content%}
        {% for post in posts %}
        <article class="media content-section">
            <div class="media-body">
                <div class="article-metadata">
                <a class="mr-2" href="#">{{ post.author }}</a>
                <small class="text-muted">{{ post.date_posted|date:"F d, Y" }}</small>
                </div>
                <h2><a class="article-title" href="#">{{ post.title }}</a></h2>
                <p class="article-content">{{ post.content }}</p>
            </div>
        </article>
        {% endfor%}
    {% endblock content%}
---

## make about page template
---
vi blog/templates/blog/about.html
{% extends "blog/base.html" %}
    {% block content%}
        <h1>Blog  About! </h1>
    {% endblock content%}
---

## Add blog application to list of installed apps
* This Change App Confiruration for Dajango to auto discover template directory in the intalled app.
* add blog config
---
blog$ vi apps.py
---
---
from django.apps import Appconfig

class BlogConfig(AppConfig)
    name='blog'
---
### add path to appconfiguration
---
dajango_project$ vi settings.py
---
---
INSTALLED_APP = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    ...
]
---

## create view; update view to load template
---
blog$vi views.py
---
---
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
---

## Create Blog URL module
---
blog$vi urls.py
---
---
from django.urls import path
form . import views

urlpatterns = [
    path('', views.home, name='blog-home')
    path('about/', views.about, name='blog-about')
]
---
## Map this url to project urls.
---
django_project$ vi urls.py
---
---
from django.contrib import admin
from dajngo.urls import path, include

urlpatterns [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]
---

# Admin Page
localhost:8000/admin 
* need to create a super user to login to admin page
* $ python manage.py createsuperuser -fails
* Reason: no such table auth_user : need to create database
* Run migration command : migration command let you make changes to database
---
$python manage.py makemigration
No changes detected
---

* i.e makemigration command detectes changes and prepare Djanogo to update the database

## apply migration
---
python manage.py migrate
---

## create super user for admin
* python mange.py createsuperuser

* run server-check the /admin login page. Try signing in

## Django DB ORM
* Object relational Mapper
* you can use different db without changing the code
* ex sqldb - dev postgre- prod
---
blog$ vi model.py
---
---
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#for storing blog posts, each class will be its own table in db
class Post(models.Models):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
---

## apply changes
---
python manage.py makemigrations
---

## view sql for migration <migration number>
---
python manage.py sqlmigrate blog 0001
---
## Migrate
---
python manage.py migrate
---
* migration allow us to make changes to database even if we have data in the database.

# working with models interactively
---
python mange.py shell
---
---
>>> from blog.models import Post
>>> from djanog.contrib.auth.models import user
>>> User.object.all()
<QuerySet>[<user: CoreyMs>, <user: TestUser>]
>>> User.objects.first()
<user: CoreyMS>
>>>User.objects.filter(username='coreyMS')
<QuerySet [<user: CoreyMS>]>
>>>User.objects.filter(username='coreyMS').first()
<user: CoreyMS>
>>> user = User.object.filter(username='coreyMS').first()
>>>user.id
1
>>>user.pk
1
>>>user = User.objects.get(id=1)
>>>user  
<User: CoreyMS>
>>>Post.objects.all()
<QuerySet []>
>>> post_1 = Post(title='Blog 1', content='First Post Content!', author=user)
>>>Post.objects.all()
<QuerySet []>
>>> post_1.save()
<QuerySet [<Post: Post object (1)>]>
>>> print("added __str()__")
addeed __str()__
>>> Post.objects.all()
<Queeryset [<Post: Blog 1>]>
>>> post_2 = Post(title='blog2', content='Second Post Content!', author_id=user.id)
>>> post_2.save()
>>> Post.objects.all()
<QuerySet[<Post: Blog 1>, <Post: Blog 2>]>
>>>post = Post.objects.first()
>>>post.content
'First Post contet!
>>>post.author
<User: CoreyMS>
>>>post.author.email
'QMS@test.com
>>>user
<user: CoryMS>
>>>user.post_set
<django.db.modes.fields.related_descriptors.create_reverse_many_to_one_manager.<locas>.RealatedManger object ad 0x1529ad03>
>>>user.post_set.all()
<QuerySet[<Post: Blog 1>, <Post Blog2>]>
>>>user.post_set.create(title='Blog3', content='Third Post Content!')
<Post: Blog3>
>>>Post.objects.all()
<QuerySet[<Post: Blog 1>, <Post:B >]>
>>>exit()
---

## Register Blog Post to admin page
---
blog$vi admin.py
---
---
from django.contrib import admin
from .models import Post

admin.site.register(Post)
---

## check
---
python3 manage.py runserver
curl localhost:8000/
curl localhost:8000/about
---
* check title for about page
* check source code - inspect elements.
* restart django
* clear cache if css is not working
* explore admin pannel


# 
## User Registaration and Login App
## style -bootstarp and form validation - cripyform - 3rd party django app (css framework)
---
djanog-project$ pip install django-crispy-forms
django-project$ python manage.py start app users
---
---
- users
  - __int__.py
  - templates
    - users
        - register.html
        - login.html
        - logout.html
        - profile.html
  - admin.py
  - apps.py
  - migrations
     - __init__.py
  - models.py
  - tests.py
  - views.py
---

djaongo_project$settings.py
INSTALLED_APP=[
  'blog.app.BlogConfig',
  'users.app.UsersConfig',
  'crispy_forms',
  ...
]

#At bottom of setting file  - overrider default bootstrap2
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'

### Dajango provide form to create new users
users$ vi views.py

from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
form djanogo.contrib import 
from djanogo.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
      form = UserRegisterForm(request.POST)
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f'Account for {username} has been created you will be able to  login now!')
           return redirect('login')
    else:
      form = UserRegisterForm()
    return render(request, 'user/registration.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
    
#now create the template. for registration.html
users$ mkdir templates
users$ mkdir templates/users
users$ vi templates/users/registration.html
{% extends "blog/base.html" %}
{% load cripsy_form_tags %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-buttom mb-4> Join Today </legend>
                {{ form|crispy }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Sign Up</button>         
            </div>
            <div class="border-top pt-3">
                <small class="text-muted">
                    Already Have an Account? <a class="ml" href="{% url 'login' %}">Sign In</a>
                </small>
            </div>        
        </form>
    </div>    
{% endblock content%}

users$ vi templates/users/login.html
{% extends "blog/base.html" %}
{% load cripsy_form_tags %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-buttom mb-4> Login </legend>
                {{ form|crispy }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Login </button>         
            </div>
            <div class="border-top pt-3">
                <small class="text-muted">
                    Need and Account <a class="ml" href="{% url 'register' %}">Sign Up Now</a>
                </small>
            </div>        
        </form>
    </div>    
{% endblock content%}

users$ vi templates/users/profile.html
{% extends "blog/base.html" %}
{% load cripsy_form_tags %}
{% block content %}
    <h1>{{ user.username }} </h1>
{% endblock content%}




users$ vi templates/users/logout.html
{% extends "blog/base.html" %}
{% block content %}
    <h2> You have been logged out </h2>
    <div class="border-top pt-3">
        <small class="text-muted">
            <a class="ml-2" href="{% url 'login' %}">Log In Again</a>
        </small>
    </div>    
{% endblock content%}

# Create URL Patten
django_project$urls.py
from django.contrib import admin
from djanog.contrib.auth import views as auth_views
from djanog.urls import path, include
form users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/' user_views.register, name='register'),
    path('profile/' user_views.profile, name='profile'),
    path('login/' auth_views.LoginView.as_view(template_name=users/login.html), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name=users/logout.html), name='logout'),
    path('', include(blog.urls)),
]

users$ vi forms.py
from django import forms
from django.contrib.auth.models import User
from djanog.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        meta = User
        fields = ['username', 'email', 'password1', 'password2']

