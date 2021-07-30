from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import login,logout,authenticate
def main(request):
    apps = Prog_level.objects.all()
    context = {
        'app': apps
    }
    return render(request, 'main.html', context)
def index(request):
    apps = Prog_level.objects.all()
    context = {
        'apps': apps
    }
    return render(request, 'index.html', context)
def practice(request):
    if request.user.username:
        form = PractitionerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('level')
        context = {
            'form':form
        }
        return render(request,'practice.html',context)
    else:
        return redirect('login')
def startup(request):
    if request.user.username:
        form = StartapperForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('level')
        context = {
            'form':form
        }
        return render(request,'startapp.html',context)
    else:
        return redirect('login') 
def developer(request):
    if request.user.username:
        form = DeveloperForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('level')
        context = {
            'form':form
        }
        return render(request,'developer.html',context)
    else:
        return redirect('login')
def regestration(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request=request,username=username,password=password)
        if user:
            profile = CustomUser.objects.create(user = user)
            profile.save()
            login(request,user)
            return redirect('login')
    context = {
        'form':form
    }
    return render(request,'sign_up.html',context)
def log_in(request):
    form = LoginForm()
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request=request, username=username, password=password)
    if user:
        login(request, user)
        func(user)
        return redirect('level')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)
def log_out(request):
    user=request.user
    if user:
        logout(request)
    return redirect('login')
def level(request):
    return render(request, 'level.html', {})
def func(user):
    p = CustomUser.objects.get(user=user)
    if p.user_type == 'practice':
        return redirect('practice')
    if p.user_type == 'startup':
        return redirect('startup')
    if p.user_type == 'developer':
        return redirect('developer')
def users(request):
    p1 = Practitioner.objects.all()
    p2 = Developer.objects.all()
    p = p1 | p2
    context = {
        'app': p
    }
    return render(request, 'main.html', context({p.username},{p.programming_language},{p.avatar}))

def saving(request):
    return render(request, 'level.html', {})