from django.forms import ModelForm, HiddenInput
from .models import Customer, Address

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = {'firstname', 'lastname'}

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'customer']
        widgets = {'customer': HiddenInput() }