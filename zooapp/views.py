from django.shortcuts import render
from decimal import Decimal
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Registration,Booking
from django.contrib.auth import authenticate,login,logout
from .forms import Signupform,Loginform,Bookingform
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.contrib import messages
from django.db.models import Sum

# Create your views here.
def home(request):
    return render(request,'home.html')

def Sign(request):
    form = Signupform()
    if request.method =='POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()   
        return redirect(login)
    return render(request,'registration.html',{'form':form})

def login(request):
    form = Loginform()
    if request.method == 'POST':
        form= Loginform(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            log = Registration.objects.filter(email=email,password=password)
            user = authenticate(request, email=email,password=password)
            if not log:
                messages.error(request,'email or password not correct')
                return render(request,'login.html')
            else:
                return redirect(logout)
        else:
            return render(request,'login.html',{'form':form})
    return render(request,'login.html',{'form':form})


def booking(request):
    form = Bookingform()
    if request.method == 'POST':
        form = Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(booklist)
    return render(request,'book.html',{'form':form})

def booklist(request):
    tick = Booking.objects.all()
    return render(request,"blist.html",{'form':tick})

def logout(request):
    return render(request,'logout.html')

def reglist(request):
    reg = Registration.objects.all()
    return render(request,"reglist.html",{'form':reg})

def count(request):
    count= Booking.objects.all().count() 
    adding=Booking.objects.all().aggregate(Sum('ticketprice'))
    return render(request,'count.html',{'count':count,"adding":adding['ticketprice__sum']})

def graph(request):
    return render(request,'graph.html')
