from django.contrib.auth import login
from django.db import models
from django.contrib.auth.models import User

CHOICES = (
    ('startapp','Startupper'),
    ('worker', 'Practical worker'),
    ('dev','Developer'),
)
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(null=True,max_length=20)
    def __str__(self):
        return self.user.username

class Practical_worker(models.Model):
    number = models.CharField(max_length=13,null=True)
    project = models.FileField()
    comment = models.TextField(max_length=2000, null=True)

class Startapp(models.Model):
    number = models.CharField(max_length=13, null=True)
    project = models.FileField()
    comment = models.TextField(max_length=2000, null=True)

class Developers(models.Model):
    number = models.CharField(max_length=13, null=True)
    project = models.FileField()
    comment = models.TextField(max_length=2000, null=True)
    # level = models.CharField(max_length=20, choices=CHOICES)
    # def __str__(self):
    #     return self.full_name

class User_details(models.Model):
    level = models.CharField(max_length=20, choices=CHOICES, null=True)
    skills = models.TextField(max_length=1000, null=True)
    image = models.ImageField()
    resume = models.FileField()