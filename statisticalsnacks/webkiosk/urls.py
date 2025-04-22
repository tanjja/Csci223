from django.http import HttpResponse
from django.urls import path
from . import views

app_name = 'webkiosk'
urlpatterns = [
    #http://localhost:8000/webkiosk/
    path('', views.index),
    
    #http://localhost:8000/webkiosk/customers/
    path('customers/', views.listcustomers, name='customer-list'),

    #http://localhost:8000/webkiosk/customers/new/
    path('customers/new/', views.addcustomer, name='customer-add'),

    #http://localhost:8000/webkiosk/customers/1/
    path('customers/<int:pk>/', views.detailcustomer, name='customer-detail'),

    #http://localhost:8000/webkiosk/customers/1/edit
    path('customers/<int:pk>/edit/', views.updatecustomer, name='customer-update'),

    #http://localhost:8000/webkiosk/customers/1/delete
    path('customers/<int:pk>/delete/', views.deletecustomer, name='customer-delete'),

    #http://localhost:8000/webkiosk/customers/1/address/new
    path('customers/<int:customer_id>/address/new', views.addaddress, name='address-add'),

]
