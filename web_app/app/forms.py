from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

# class ChooseForm(forms.Form):
#     level = forms.CharField(label='Choice your level', widget=forms.Select(choices=CHOICES))
# class StartupForm(forms.ModelForm):
#     class Meta:
#         model = Startapp
#         fields = '__all__'
# class PracticeForm(forms.ModelForm):
#     class Meta:
#         model = Practical_worker
#         fields = '__all__'
class StartupForm(forms.Form):
    title = forms.CharField(label='Title', max_length=200)
    number = forms.CharField(label='Number',max_length=13)
    project = forms.FileField(label='Project file')
    comment =forms.TimeField(label='Description')
    image = forms.ImageField(label='Your image')
    
class Prog_levelForm(forms.ModelForm):
    class Meta:
        model = Prog_level
        fields = ['title','project','comment','skills','level','type_work','resume','image']
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
