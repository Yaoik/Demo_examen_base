from django.contrib import auth
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from users.forms import CustomUserLogin, CustomUserRegister
from django.core.handlers.wsgi import WSGIRequest


def login(request:WSGIRequest):
    if request.method == 'POST':
        form = CustomUserLogin(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = CustomUserLogin()
        
        
    context = {
        'title': 'Home - login',
        'form': form,
    }
    
    return render(request, 'users/login.html', context=context)


def register(request:WSGIRequest):
    if request.method == 'POST':
        form = CustomUserRegister(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user=user)
            return redirect(reverse('main:index'))
    else:
        form = CustomUserRegister()
        
    context = {
        'title': 'Home - register',
        'form': form
    }
    
    return render(request, 'users/register.html', context=context)


@login_required
def profile(request:WSGIRequest):
    
    context = {
        'title':'Home - profile'
    }
    return render(request, 'users/profile.html', context=context)


@login_required
def logout(request:WSGIRequest):
    auth.logout(request)
    return redirect(reverse('main:index'))


    