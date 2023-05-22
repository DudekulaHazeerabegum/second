from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def aajju(request):
    return HttpResponse('<marquee><h1>hi,good morning</h1></marquee>')
def nani(request):
    return HttpResponse('<marquee>GOOD BOY</marquee>')
     