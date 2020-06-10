from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import Flight

# Create your views here.
def index(request):
    context={
      "flights":Flight.objects.all()  
    }
   

    return render (request,"flights/index.html",context)
