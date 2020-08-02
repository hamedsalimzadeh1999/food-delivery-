from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# from .models import PizzaModel,CustomerModel,OrderModel


def adminloginview(request):
    return render(request,'login.html')

def adminauth(request,):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username = username,password = password)
    if user is None:
        messages.add_message(request,messages.ERROR,"invalid password")
        return redirect('adminlogin')

    else :
        login(request,user)
        return redirect("adminpage")

def logoutadmin(request):
    logout(request)
    return redirect('adminlogin')

def adminpage (request):
    return render(request,'admin.html')
