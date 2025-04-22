from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'webkiosk/base_template.html')

def listcustomers(request):
    customerlist = Customer.objects.all()
    context = {'customerlist': customerlist }
    return render(request, 'webkiosk/customer_list.html', context)

def listfood(request):
    foodlist = Food.objects.all()
    context = {'foodlist': foodlist }
    return render(request, 'webkiosk/food_list.html', context)

def addcustomer(request):
    if request.method == 'GET':
        cf = CustomerForm()
    elif request.method == 'POST':
        cf = CustomerForm(request.POST)
        if cf.is_valid():
            cf.save()
            return redirect('webkiosk:customer-list')
           
    context = { 'form': cf, 'actionname': 'Add'}
    return render(request, 'webkiosk/customer_form.html', context)

def addfood(request):
    if request.method == 'GET':
        ff = FoodForm()
    elif request.method == 'POST':
        ff = FoodForm(request.POST)
        if ff.is_valid():
            ff.save()
            return redirect('webkiosk:food-list')
           
    context = { 'form': ff, 'actionname': 'Add'}
    return render(request, 'webkiosk/food_form.html', context)


def detailcustomer(request, pk):
    c = Customer.objects.get(id=pk)
    context = {'customer': c}
    return render(request, 'webkiosk/customer_detail.html', context)

def detailfood(request, pk):
    f = Food.objects.get(id=pk)
    context = {'food': f}
    return render(request, 'webkiosk/food_detail.html', context)

def updatecustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'GET':
        form = CustomerForm(instance=customer)
    elif request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer record updated successfully.') 
            return redirect('webkiosk:customer-list')

    context = {'form': form, 'actionname': 'Edit'}
    return render(request, 'webkiosk/customer_form.html', context)

def updatefood(request, pk):
    food = Food.objects.get(id=pk)
    if request.method == 'GET':
        form = FoodForm(instance=food)
    elif request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food record updated successfully.') 
            return redirect('webkiosk:food-list')

    context = {'form': form, 'actionname': 'Edit'}
    return render(request, 'webkiosk/food_form.html', context)

def deletecustomer(request, pk):
    c = get_object_or_404(Customer, id=pk) 
    if request.method == 'GET':
        context = {'customer': c }
        return render(request, 'webkiosk/customer_delete.html', context)
    
    elif request.method == 'POST':  
        c.delete()
        return redirect('webkiosk:customer-list')
    
def deletefood(request, pk):
    f = get_object_or_404(Food, id=pk) 
    if request.method == 'GET':
        context = {'food': f }
        return render(request, 'webkiosk/food_delete.html', context)
    
    elif request.method == 'POST':  
        f.delete()
        return redirect('webkiosk:food-list')
    
def addaddress(request, customer_id):
    if request.method == 'GET':
        customer = get_object_or_404(Customer, id=customer_id)
        form = AddressForm(initial={'customer':customer})
    elif request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            print("test")
            return redirect('webkiosk:customer-detail',pk=customer_id)
        else:
            print(form.errors)

    context = { 'form': form }
    return render(request, 'webkiosk/address_form.html', context)

def addorder(request):
    if request.method == 'GET':
        of = OrderForm()
    elif request.method == 'POST':
        of = OrderForm(request.POST)
        if of.is_valid():
            order = of.save()
            return redirect('webkiosk:order-detail', order_id=order.id)
           
    context = { 'form': of, 'actionname': 'Add'}
    return render(request, 'webkiosk/order_form.html', context)

def addorderitem(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'GET':
        form = OrderItemForm()
    elif request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.order = order
            item.save()
            return redirect('webkiosk:order-detail', order_id=order_id)

    context = { 'form': form, 'order':order}
    return render(request, 'webkiosk/order_item_form.html',context)

def orderdetail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    items = order.orderitem_set.all()

    for item in items:
        item.subtotal = item.quantity * item.food.price

    total_price = sum(item.subtotal for item in items)

    context = {'order': order, 'items': items, 'total_price': total_price}

    return render(request, 'webkiosk/order_detail.html', context)


def editorderitem(request, pk):
    item = get_object_or_404(OrderItem, pk=pk)
    if request.method == 'GET':
        form = OrderItemForm(instance=item)
    elif request.method == 'POST':
        form = OrderItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('webkiosk:order-detail', order_id=item.order.id)
        
    return render(request, 'webkiosk/order_item_form.html', {'form': form, 'order': item.order})

def deleteorderitem(request, pk):
    item = get_object_or_404(OrderItem, pk=pk)
    order_id = item.order.id
    item.delete()
    context = {'actionname': 'Add'}
    return redirect('webkiosk:order-detail', order_id=order_id)

def listorders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'webkiosk/order_list.html', context)

def updateorder(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('webkiosk:order-detail', order_id=order.id)
    else:
        form = OrderForm(instance=order)

    context = {'form': form, 'order': order, 'actionname': 'Edit'}
    return render(request, 'webkiosk/order_form.html', context)

def deleteorder(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('webkiosk:order-list')