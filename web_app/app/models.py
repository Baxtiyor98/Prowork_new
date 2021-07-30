from django.contrib.auth import login
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
USER_TYPE = (
    ('startap', 'Startupper'),
    ('practice', 'Practitioner'),
    ('developer','Developer'),
)
Choice_type = (
    ('Offline', 'Offline'),
    ('Online','Online'),
)
class CustomUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    bio = models.TextField(default="No bio...")
    user_type = models.CharField(max_length=20,null=True,choices=USER_TYPE)
    def __str__(self):
        return str(self.user)
    
class Startapper(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,unique=True)
    title = models.CharField(max_length=100, null=True)
    project = models.FileField(upload_to='project', blank=True,null=True)
    comment = models.TextField(default='No comment...',max_length=2000, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True,unique=True)
    avatar = models.ImageField(upload_to='avatar',default="static 'avatar.png'", blank=True,null=True)
    def __str__(self):
        return str(f"{self.user}"+" and "+f"{self.title}")
    
class Practitioner(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,unique=True)
    title = models.CharField(max_length=100, null=True)
    project = models.FileField(upload_to='project', blank=True,null=True)
    comment = models.TextField(default='No comment...',max_length=2000,blank=True,null=True)
    number = models.CharField(max_length=20, null=True)
    programming_language = models.CharField(default='',max_length=200, blank=True, null=False)
    user_type = models.CharField(max_length=20,null=True,choices=USER_TYPE)
    # On_Off = models.CharField(max_length=20, default='', choices=Choice_type)
    avatar = models.ImageField(upload_to='avatar/',default="static 'avatar.png'", blank=True,null=True)
    resume = models.FileField(upload_to='resume',null=True)
    def __str__(self):
        return str(self.user)
    

class Developer(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100, null=True)
    project = models.FileField(upload_to='project',null=True)
    comment = models.TextField(default='No comment...',max_length=2000,blank=True,null=True)
    number = models.CharField(max_length=20, null=True)
    programming_language = models.CharField(max_length=200, null=True)
    user_type = models.CharField(max_length=20, null=True, choices=USER_TYPE)
    # On_Off = models.CharField(max_length=20, choices=Choice_type)
    avatar = models.ImageField(upload_to='avatar',default="static 'avatar.png'", blank=True,null=True)
    resume = models.FileField(upload_to='resume',null=True)
    def __str__(self):
        return str(f"{self.user}")
class Prog_level(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=13, null=True)
    project = models.FileField(upload_to='project',null=True)
    comment = models.TextField(max_length=2000, null=True)
    level = models.CharField(max_length=20, choices=USER_TYPE,null=True)
    skills = models.CharField(max_length=200, null=True)
    avatar = models.ImageField(upload_to='avatar',null=True)
    resume = models.FileField(upload_to='resume',null=True)
    type_work = models.CharField(max_length=20, choices=Choice_type,null=True)
    def __str__(self):
        return str(self.user)