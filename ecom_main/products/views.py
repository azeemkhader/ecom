from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    featured_products=Products.objects.order_by('priority')[:4]
    latest_products=Products.objects.order_by('-id')[:4]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(request,'index.html',context)

def product_page(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Products.objects.all()
    product_paginator=Paginator(product_list,1)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request,'products.html',context)


def product_detail(request,id):
    product=Products.objects.get(id=id)
    context={'products':product}
    return render(request,'product_detail.html',context)