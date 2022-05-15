from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from BloodBankApp.models import donate


def Home(request):
    return render(request,'Base.html')

def Registration(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if username and password:
            if password==password1:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'username already exist')
                    return redirect('/Registration')
                else:
                    user=User.objects.create_user(username=username,password=password)
                    user.save()
                    return redirect('/Login')

            else:
                messages.info(request,'password not matched')
                return redirect('/Registration')
        else:
            return redirect('/Registration')


    return render(request,'Registration.html')

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/Donation')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/Login')

    return render(request,'Login.html')

def Donation(request):

    if request.method=='POST':
        name=request.POST['name']
        gender=request.POST['gender']
        age=request.POST['age']
        phno=request.POST['pnumber']
        email=request.POST['mail']
        address=request.POST['address']
        district=request.POST['district']
        sub=request.POST['sub']
        bloodgrp=request.POST['bloodgrp']


        if name and gender and age and phno and email and address and bloodgrp:
            don = donate(name=name, gender=gender, age=age, phno=phno, email=email, address=address, district=district,
                         sub=sub, bloodgrp=bloodgrp)
            don.save()
            html = "<html><body><h1 style='text-align:center'>Booking Confirmed You Can Donate Blood</h1><h1 style='text-align:center'><button><a href='/'><h4>Home</h4></a></button></h1></body></html>"
            return HttpResponse(html)
        else:
            return redirect('/Donation')






    return render(request,'Donation.html')

def Logout(request):
    auth.logout(request)
    return redirect('/')

