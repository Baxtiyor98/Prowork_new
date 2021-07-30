from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class StartapperForm(forms.ModelForm):
    class Meta:
        model = Startapper
        fields = '__all__'
class PractitionerForm(forms.ModelForm):
    class Meta:
        model = Practitioner
        fields = '__all__'
class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = '__all__'
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
