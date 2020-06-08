from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    print(os.environ['PASSWORD'])

    return HttpResponse ("hello")
