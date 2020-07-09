from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
import os
from .models import Flight,Airport,Passenger
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout 

# Create your views here.

def log(request):
    if not request.user.is_authenticated:
        return render(request,"flights/login.html",{"message":None})
    
    context={
        "user":request.user
    }
    return render(request,"flights/user.html",context) 

def login_view(request):
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"flights/login.html",{"message":"invalid credential." })      




def logout_view(request):
    logout(request)
    return render(request,"flights/login.html",{"message":"Logged out"})

def index(request):
    context={
      "flights":Flight.objects.all()  
    }
   

    return render (request,"flights/index.html",context)

def flight(request,flight_id):
    try:
        flight=Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist.")
    context={
        "flight":flight,
        "passengers":flight.passengers.all(),
        "non_passengers":Passenger.objects.exclude(flights=flight).all()
    }
    return render (request,"flights/flight.html",context)


def book(request,flight_id):
    try:
        passenger_id=int(request.POST["passenger"])
        passenger=Passenger.objects.get(pk=passenger_id)
        flight=Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request,"flights/error.html",{"message":"No selection"})

    
    except Flight.DoesNotExist:
        return render(request,"flights/error.html",{"message":"No flight"})
    
    except Passenger.DoesNotExist:
        return render(request,"flights/error.html",{"message":"No Passenger"})

    passenger.flights.add(flight) 
    return HttpResponseRedirect(reverse("flight",args=(flight_id,))) 




