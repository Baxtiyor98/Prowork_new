from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import login,logout,authenticate
def main(request):
    apps = Startapp.objects.all()
    context = {
        'app': apps
    }
    return render(request, 'main.html', context)
def index(request):
    apps = Developers.objects.all()
    context = {
        'apps': apps
    }
    return render(request, 'index.html', context)
def choice(request):
    form = ChooseForm()
    context = {
        'form':form
    }
def startup(request):
    if request.user.username:
        form = StartupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('level')
        context = {
            'form':form
        }
        return render(request,'startapp.html',context)
    else:
        return redirect('login')
def practice(request):
    form = PracticeForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('level')
    context = {
        'form':form
    }
    return render(request,'practice.html',context)   
def developer(request):
    if request.user.username:
        form = DeveloperForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_details')
        context = {
            'form':form
        }
        return render(request,'developer.html',context)
    else:
        return redirect('login')
def user_details(request):
    if request.user.username:
        form = User_detailsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('level')
        context = {
            'form':form
        }
        return render(request,'developer.html',context)
    else:
        return redirect('sign_up')
def regestration(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request=request,username=username,password=password)
        if user:
            profile = Profile.objects.create(user = user)
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
