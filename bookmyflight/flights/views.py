from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import os
from .models import Flight,Airport,Passenger
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForms,PassengerForm

# Create your views here.
def log(request):
    if not request.user.is_authenticated:
        return render(request,"flights/login1.html",{"message":None})
    
    context={
        "user":request.user
    }
    return render(request,"flights/landing.html",context) 

def login_view(request):
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse("log"))
    else:
        return render(request,"flights/login1.html",{"message":"invalid credential." })      




def logout_view(request):
    logout(request)
    return render(request,"flights/login1.html",{"message":"Logged out"})


def registerPage(request):
    form=CreateUserForms()
    
    if request.method == 'POST':
        form = CreateUserForms(request.POST)
        if form.is_valid():
            form.save()
    
    context={"form":form}
    return render(request,"flights/register.html",context)



def flights_view(request):
    context={
      "flights":Flight.objects.all()  
    }
   

    return render (request,"flights/flightsinfo.html",context)

def signup_view(request):
    return render(request,"flights/register.html")


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
    return render (request,"flights/flightdetail.html",context)


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

def addpassenger(request):
    form=PassengerForm()
    if request.method=='POST':
        form=PassengerForm(request.POST)
        if form.is_valid():
            form.save()


        

        
    context={'form':form}

    return render(request,"flights/booking.html",context)

def aboutus(request):
    return render(request,"flights/about.html")


def contactus(request):
    return render(request,"flights/contact.html")
        




