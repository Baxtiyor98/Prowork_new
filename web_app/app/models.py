from django.contrib.auth import login
from django.db import models
from django.contrib.auth.models import User

CHOICES = (
    ('practice', 'Practical worker'),
    ('developer','Developer'),
)
Choice_type = (
    ('Offline', 'Offline'),
    ('Online','Online'),
)

class Prog_level(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=13, null=True)
    project = models.FileField(null=True)
    comment = models.TextField(max_length=2000, null=True)
    level = models.CharField(max_length=20, choices=CHOICES,null=True)
    skills = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True)
    resume = models.FileField(null=True)
    type_work = models.CharField(max_length=20, choices=Choice_type,null=True)