from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include 
from . import views
from .views import MessageChannel
# Create your views here.
urlpatterns = [
    path('addmessage/', MessageChannel.as_view()),
]