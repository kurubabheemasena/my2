from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bheema(request):
    return HttpResponse('<h1><marquee>bheemasena</marquee></h1>')
