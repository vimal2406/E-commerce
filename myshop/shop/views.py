from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nslides = n//4 + ceil((n/4)-(n/4))
    # params = {'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    allProds = [[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    params = {'allProds':allProds}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("We are on contact page")
def tracker(request):
    return HttpResponse("We are on track product page")

def productview(request):
    return HttpResponse("We are on product Overview page")

def checkout(request):
    return HttpResponse("We are on checkout page")

def search(request):
    return HttpResponse("We are on search page")