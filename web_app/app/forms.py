from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class ChooseForm(forms.Form):
    level = forms.CharField(label='Choice your level', widget=forms.Select(choices=CHOICES))
class StartupForm(forms.ModelForm):
    class Meta:
        model = Startapp
        fields = '__all__'
class PracticeForm(forms.ModelForm):
    class Meta:
        model = Practical_worker
        fields = '__all__'

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developers
        fields = '__all__'
class User_detailsForm(forms.ModelForm):
    class Meta:
        model = User_details
        fields = '__all__'
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
