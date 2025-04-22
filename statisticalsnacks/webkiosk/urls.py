from django.http import HttpResponse
from django.urls import path
from . import views

app_name = 'webkiosk'
urlpatterns = [
    #http://localhost:8000/webkiosk/
    path('', views.index),
    
    #http://localhost:8000/webkiosk/customers/
    path('customers/', views.listcustomers, name='customer-list'),

    #http://localhost:8000/webkiosk/food/
    path('food/', views.listfood, name='food-list'),

    #http://localhost:8000/webkiosk/customers/new/
    path('customers/new/', views.addcustomer, name='customer-add'),

    #http://localhost:8000/webkiosk/food/new/
    path('food/new/', views.addfood, name='food-add'),

    #http://localhost:8000/webkiosk/customers/1/
    path('customers/<int:pk>/', views.detailcustomer, name='customer-detail'),

    #http://localhost:8000/webkiosk/food/1/
    path('food/<int:pk>/', views.detailfood, name='food-detail'),

    #http://localhost:8000/webkiosk/customers/1/edit
    path('customers/<int:pk>/edit/', views.updatecustomer, name='customer-update'),

    #http://localhost:8000/webkiosk/food/1/edit
    path('food/<int:pk>/edit/', views.updatefood, name='food-update'),

    #http://localhost:8000/webkiosk/customers/1/delete
    path('customers/<int:pk>/delete/', views.deletecustomer, name='customer-delete'),

    #http://localhost:8000/webkiosk/food/1/delete
    path('food/<int:pk>/delete/', views.deletefood, name='food-delete'),

    #http://localhost:8000/webkiosk/customers/1/address/new
    path('customers/<int:customer_id>/address/new', views.addaddress, name='address-add'),

    #http://localhost:8000/webkiosk/orders//new
    path('orders/new/', views.addorder, name='order-add'),

    #http://localhost:8000/webkiosk/order/1/
    path('orders/<int:order_id>/', views.orderdetail, name='order-detail'),

    #http://localhost:8000/webkiosk/order/1/add-item/
    path('orders/<int:order_id>/add-item/', views.addorderitem, name='orderitem-add'),

    path('orderitem/<int:pk>/edit/', views.editorderitem, name='orderitem-edit'),

    path('orderitem/<int:pk>/delete/', views.deleteorderitem, name='orderitem-delete'),

    path('orders/', views.listorders, name='order-list'),

    path('orders/<int:order_id>/edit/', views.updateorder, name='order-update'),

    path('orders/<int:order_id>/delete/', views.deleteorder, name='order-delete'),
]
