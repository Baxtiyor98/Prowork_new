from django import forms
from django.contrib import admin
from .models import *
admin.site.register(CustomUser)
admin.site.register(Startapper)
admin.site.register(Practitioner)
admin.site.register(Developer)