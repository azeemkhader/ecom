from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request,'index.html')

def product_page(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Products.objects.all()
    product_paginator=Paginator(product_list,1)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request,'products.html',context)


def product_detail(request):
    return render(request,'product_detail.html')