from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil, prod

# Create your views here.
def index(request):
    allProds =[]
    # products = Product.objects.all()
    # print(products)
    catprods = Product.objects.values('category','product_id')
    cats = {item['category'] for item in catprods}
    for cats in cats:
        prod = Product.objects.filter(category=cats)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n/4))
        allProds.append([prod, range(1,nslides),nslides])
    # params = {'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    # allProds = [[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    params = {'allProds':allProds}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
     return render(request,'shop/contact.html')

def tracker(request):
     return render(request,'shop/tracker.html')

def productView(request,myid):
     product=Product.objects.filter(id=myid)
     print(product)
     return render(request,'shop/prodView.html',{'product':product[0]})

def checkout(request):
     return render(request,'shop/checkout.html')

def search(request):
     return render(request,'shop/search.html')