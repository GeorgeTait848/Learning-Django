from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
#this view is called when the user is directed to the blog home page, hence the name home. 
    context = {'posts': Post.objects.all(), 'title': 'Home'}
    return render(request, 'blog/home.html', context)

def about(request): 

    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)