from django.shortcuts import render, HttpResponse,redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def ecommerce(request):
    data = Product.objects.filter(category="Featured")
    context = {
        'data':data
    }
    return render(request,"e-commerce.html",context)

def loginhandle(request):
    if request.method == "POST":
        uname = request.POST['username']
        passw = request.POST['password']
        user = authenticate(username = uname, password = passw)
        print(user, "user>>>>>><<<<<<<")
        if user is not None:
            login(request,user)
            return redirect('/')

    return render(request,"login.html")

def logoutHandle(request):
    logout(request)
    return redirect('/')

def signuphandle(request):
    if request.method=="POST":
        uname = request.POST['username']
        email = request.POST['email']
        passw = request.POST['password']
        if User.objects.filter(username = uname).first():
            messages.success(request,'Username already taken!!!!')
        else:
            print(uname , email , passw)
            user = User(username=uname, email=email)
            user.set_password(passw)
            user.save()
            messages.success(request,"Acount Create Sucessfull")
    return render(request,"signup.html")

def checkout(request):
    return render(request,"checkout.html")
def cart(request):
    return render(request,"cart.html")

def product_des(request,id):
    print(id)
    get_product_data = Product.objects.filter(id =id)
    context = {
        'pdata':get_product_data
    }
    return render(request,"productdescription.html",context)
def men(request):
    return render(request,"men.html")
def about(request):
    return render(request,"aboutus.html")
def contact(request):
    return render(request,"contact.html")

def men(request):
    data = Product.objects.filter(category="Men")
    # for i in data:
    #     print(i.title)
    #     print(i.size)
    #     print(i.description)
    #     print(i.price)
    context = {
        'data':data
    }
    return render(request,'men.html',context)

def women(request):
    data = Product.objects.filter(category="Women")
    # for i in data:
    #     print(i.title)
    #     print(i.size)
    #     print(i.description)
    #     print(i.price)
    context = {
        'data':data
    }
    return render(request,'women.html',context)
def kids(request):
    data = Product.objects.filter(category="Kids")
    # for i in data:
    #     print(i.title)
    #     print(i.size)
    #     print(i.description)
    #     print(i.price)
    context = {
        'data':data
    }
    return render(request,'kids.html',context)