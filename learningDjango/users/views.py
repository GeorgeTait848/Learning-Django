from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account Created! You are now able to log in!')
            return redirect('login') #refers to the name attribute of the url pattern we wish to redirect to. 
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form
    }

    return render(request, 'users/register.html', context=context)

@login_required
def profile(request): 
    return render(request, 'users/profile.html')