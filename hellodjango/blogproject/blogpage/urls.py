from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.blog, name='blog'),
    path('about/', views.about, name='blog-about'),
]
