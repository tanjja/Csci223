from django.db import models

# Create your models here.

class Customer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return f' CUSTOMER #{self.id} NAME: {self.firstname} {self.lastname} DATE JOINED: {self.date_joined}'
        
class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self): 
        return f'CUSTOMER: {self.customer.firstname} {self.customer.lastname}, ADDRESS: {self.street} {self.city}'