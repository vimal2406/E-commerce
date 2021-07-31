from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'shop/index.html')

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