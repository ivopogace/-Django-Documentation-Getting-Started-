from django.shortcuts import render

from django.contrib import admin

# Register your models here.
from polls.models import Question, Car

admin.site.register(Question)
admin.site.register(Car)
