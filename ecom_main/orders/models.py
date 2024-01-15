from django.db import models
from customers.models import Customers
from products.models import Products
# Create your models here.

class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    ORDER_STATUS=((ORDER_PROCCESSED,'ORDER_PROCCESSED'),
                  (ORDER_DELIVERED,'ORDER_DELIVERED'),
                  (ORDER_REJECTED,'ORDER_REJECTED')
                  )
    order_status=models.IntegerField(choices=ORDER_STATUS,default=CART_STAGE)
    owner=models.ForeignKey(Customers,on_delete=models.SET_NULL,null=True,related_name='owner_user')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,related_name='added_carts')
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')
       
