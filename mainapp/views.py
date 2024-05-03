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