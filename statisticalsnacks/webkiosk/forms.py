from django.forms import ModelForm, HiddenInput
from .models import *
from django import forms

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'customer']
        widgets = {
            'customer': HiddenInput(),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}), 
        }
    
class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'price', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'paymentmode',]
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'paymentmode': forms.Select(attrs={'class': 'form-control'}),
        } 

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['food', 'quantity']
        widgets = {
            'food': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }