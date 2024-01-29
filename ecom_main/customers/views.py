from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from . models import Customers

# registration and collection of client data 
def sign_out(request):
      logout(request)
      return redirect('home')
      

    
def account(request):
    context={}
    if request.POST and 'register' in request.POST:
            context['register']=True
            try:
                username=request.POST.get('username')
                password=request.POST.get('password')
                address=request.POST.get('address')
                phone=request.POST.get('phone')
                email=request.POST.get('email')

                # creation of user account 
                user=User.objects.create_user(
                    username=username,
                    password=password,

                )

                customer=Customers.objects.create(
                    user=user,
                    address=address,
                    phone=phone

                )
                success_message='user created  successfully'
                messages.success(request,success_message)
            except Exception as e:
                error_message='username already exits'
                messages.error(request,error_message)
     
    if request.POST and 'login' in request.POST:
             context['register']=False

             username=request.POST.get('username')
             password=request.POST.get('password')
             user=authenticate(username=username,password=password)
             print(user)
             if user:
                   login(request,user)
                   return redirect('home')
             
             else:
                    
                    messages.error(request,'login failed')

     
                    
          
          
                   

        

    return render(request,'account.html',context)


