from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include 
from . import views
# Create your views here.
urlpatterns = [
     path('', views.home, name ="home"),
     path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),

]