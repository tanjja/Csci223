from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Customer, Address
from .forms import CustomerForm, AddressForm
# Create your views here.

def index(request):
    return render(request, 'webkiosk/base_template.html')

def listcustomers(request):
    customerlist = Customer.objects.all()
    context = {'customerlist': customerlist }
    return render(request, 'webkiosk/customer_list.html', context)

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

def detailcustomer(request, pk):
    c = Customer.objects.get(id=pk)
    context = {'customer': c}
    return render(request, 'webkiosk/customer_detail.html', context)

def updatecustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'GET':
        form = CustomerForm(instance=customer)
    elif request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer record updated successfully.') 

    context = {'form': form, 'actionname': 'Edit'}
    return render(request, 'webkiosk/customer_form.html', context)

def deletecustomer(request, pk):
    c = get_object_or_404(Customer, id=pk) 
    if request.method == 'GET':
        context = {'customer': c }
        return render(request, 'webkiosk/customer_delete.html', context)
    
    elif request.method == 'POST':  
        c.delete()
        return redirect('webkiosk:customer-list')
    
def addaddress(request, customer_id):
    if request.method == 'GET':
        customer = get_object_or_404(Customer, id=customer_id)
        form = AddressForm(initial={'customer':customer})
    elif request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()

    context = { 'form': form }
    return render(request, 'webkiosk/address_form.html', context)