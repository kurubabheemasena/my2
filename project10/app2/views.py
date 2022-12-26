from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def day(request):
    return HttpResponse('<marquee><h1>RAMASWAMY</marquee></h1>')
