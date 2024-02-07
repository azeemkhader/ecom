from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('cart/', views.cart_display,name='cart'), 
    path('add_to_cart/', views.add_to_cart,name='add_to_cart'),
    path('remove_item<pk>/', views.remove_from_cart,name='remove_from_cart'),
    path('cart/checkout/', views.checkout,name='checkout'),
    


]