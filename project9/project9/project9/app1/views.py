from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def malli(request):
    return HttpResponse('<marquee><h1>mallikarjuna</h1></marquee>')