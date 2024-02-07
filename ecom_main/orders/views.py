from django.shortcuts import render,redirect
from . models import Order,OrderItem
from products.models import Products
from django.contrib import messages


# Create your views here.

def cart_display(request):

        user=request.user
        customer=user.customer_profile
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        context={'cart':cart_obj}
    


        return render(request,'cart.html',context)

def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity') )
        product_id=request.POST.get('product_id')
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product=Products.objects.get(pk=product_id)
        ordered_item,created=OrderItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
           

        )
        if created:
             ordered_item.quantity=quantity
             ordered_item.save()
        else:
             ordered_item.quantity=ordered_item.quantity+quantity
             ordered_item.save()

                  
    return redirect('cart')

def remove_from_cart(request,pk):
     item=OrderItem.objects.get(pk=pk)
     if item :
          item.delete()

     return redirect('cart')     

def checkout(request) :
      if request.POST:
           try:
                user=request.user
                customer=user.customer_profile
                total=float(request.POST.get('total') )
                cart_obj=Order.objects.get(
                    owner=customer,
                    order_status=Order.CART_STAGE
                )
                if cart_obj:
                    cart_obj.order_status=Order.ORDER_CONFIRMED
                    cart_obj.save()
                    status_message="Thanks, Your order has been confirmed "
                    messages.success(request,status_message)
                else:
                    status_messages='Order not confirmed '
                    messages.error(request,status_messages)


           except Exception as e:
                status_message='Order not confirmed ' 
                messages.error(request,status_message)

      return redirect('cart')


           
            
       
             

          