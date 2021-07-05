from django.contrib.auth import login
from django.db import models
from django.contrib.auth.models import User

CHOICES = (
    ('practice', 'Practical worker'),
    ('startup','Startupper'),
    ('developer','Developer'),
)

# class Practical_worker(models.Model):
#     number = models.CharField(max_length=13,null=True)
#     project = models.FileField()
#     comment = models.TextField(max_length=2000, null=True)

# class Startapp(models.Model):
#     number = models.CharField(max_length=13, null=True)
#     project = models.FileField()
#     comment = models.TextField(max_length=2000, null=True)

class Prog_level(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    number = models.CharField(max_length=13, null=True)
    project = models.FileField(null=True)
    comment = models.TextField(max_length=2000, null=True)
    level = models.CharField(max_length=20, choices=CHOICES,null=True)
    skills = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True)
    resume = models.FileField(null=True)