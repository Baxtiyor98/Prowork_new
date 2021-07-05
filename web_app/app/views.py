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
def choice(request):
    form = ChooseForm()
    context = {
        'form':form
    }
def practice(request):
    if request.user.username:
        form = Prog_levelForm(request.POST,request.FILES)
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
    form = StartupForm()
    if request.method == 'POST':
        # print(request.POST,request.FILES)
        prog_level = Prog_level.objects.get(user=request.user)
        prog_level.number = request.POST.get('number')
        prog_level.comment = request.POST.get('comment')
        prog_level.project = request.FILES.get('project')
        prog_level.image = request.FILES.get('image')
        prog_level.save()
        print('image... ',prog_level.image)
        return redirect('level')
    context = {
        'form':form
    }
    return render(request,'startapp.html',context)   
def developer(request):
    if request.user.username:
        form = Prog_levelForm(request.POST,request.FILES)
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
            profile = Prog_level.objects.create(user = user)
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
    p = Prog_level.objects.get(user=user)
    if p.level == 'practice':
        return redirect('practice')
    if p.level == 'startup':
        return redirect('startup')
    if p.level == 'developer':
        return redirect('developer')