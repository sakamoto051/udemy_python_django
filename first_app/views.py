from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print(__file__)
    return HttpResponse('Hello World!')