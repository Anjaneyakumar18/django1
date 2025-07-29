from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world! This is the home page.")

def home2(request):
    return HttpResponse("This is the alternative home page.")

def home3(request):
    return HttpResponse("<h1>I am ak</h1><h2>I am batman </h2>")
