from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import pizza ,Customer


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

def add_pizza(request):
    title = request.POST.get('title')
    price = request.POST.get('price')
    info  = request.POST.get('info')
    pizza(title = title , price = price , info = info).save()
    return redirect("adminpage")
    
def viewpizaa(request):
    pizzalist = pizza.objects.all()
    context = {"pizzalist":pizzalist}
    return render(request , "listview.html", context )
def editpizaa(request,pizzaid):
    context = {'pizzaid':pizzaid}
    title = request.POST.get('title')
    price = request.POST.get('price')
    info  = request.POST.get('info')
    order = pizza.objects.filter(id = pizzaid)[0]
    order.title = title
    order.price  = price 
    order.info   = info  
    order.save()
    return redirect('pizzaview')
def deletepizaa(request,pizzaid):
    context = {'pizzaid':pizzaid}
    pizza.objects.filter(id = pizzaid)[0].delete()
    return redirect('pizzaview')
def HomePage(request):
    return render(request ,"index.html")
def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phonenumber = request.POST['phonenumber']
    if User.objects.filter(username =username).exists():
        messages.add_message(request,messages.ERROR,"user exiest")
        return redirect('index')
    User.objects.create_user(username = username , password=password).save()
    lastobject = len(User.objects.all())-1
    Customer(Customerid = User.objects.all()[lastobject].id,PhoneNumber=phonenumber)
    messages.add_message(request,messages.ERROR,"user make")
    return redirect('index')
def coustomerpage (request):
    context ={'pizza' : pizza.objects.all()}
    return render(request,'userpage.html',context)
def loginuser(request):
    return render(request,'userlogin.html')
def userauth (request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username = username,password = password)
    if user is None:
        messages.add_message(request,messages.ERROR,"invalid password")
        return redirect('userlogin')

    else :
        login(request,user)
        messages.add_message(request,messages.ERROR,f'welcome {user}')
        return redirect("userpage")

def logoutuser(request):
    return redirect('index')