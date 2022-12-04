from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Created account for {}!'.format(username))
            return redirect('blog-home') #refers to the name attribute of the url pattern we wish to redirect to. 
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form
    }

    return render(request, 'users/register.html', context=context)