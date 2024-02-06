from django.shortcuts import render
from cart.models import Product

def index(request):
    product=Product.objects.all()
    return render (request,'../templates/index.html',{'product':product})