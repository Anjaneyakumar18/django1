from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world! This is the home page.")

def home2(request):
    return HttpResponse("This is the alternative home page.")