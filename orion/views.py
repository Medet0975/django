from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    hello = '<h1>Dear my friends</h1>'
    return HttpResponse(hello)

def about(request):
    return HttpResponse('<h2>Today I made my first project by django</h2>')

def contact(request):
    return HttpResponse('<h3>Yours, Mr. M.A.</h3>')


# Create your views here.
