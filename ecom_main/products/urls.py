from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index,name='home'),
    path('products/', views.product_page,name='product_page'),
    path('product_details/', views.product_detail,name='product_detail')


]