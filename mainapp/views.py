from django.shortcuts import render
from .models import Product
# Create your views here.

def ecommerce(request):
    return render(request,"e-commerce.html")

def loginhandle(request):
    return render(request,"login.html")

def signuphandle(request):
    return render(request,"signup.html")
def checkout(request):
    return render(request,"checkout.html")
def cart(request):
    return render(request,"cart.html")

def product_des(request):
    return render(request,"productdescription.html")
def men(request):
    return render(request,"men.html")
def about(request):
    return render(request,"aboutus.html")
def contact(request):
    return render(request,"contact.html")

def men(request):
    data = Product.objects.all()
    for i in data:
        print(i.title)
        print(i.size)
        print(i.description)
        print(i.price)
    return render(request,'men.html')