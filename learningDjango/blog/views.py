from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
#this view is called when the user is directed to the blog home page, hence the name home. 
    return HttpResponse('<h1> Blog Home </h1>')

def about(request): 
    return HttpResponse('<h1>Blog About</h1>')