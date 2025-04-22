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

class Food(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return(f"Food Name: {self.name}\nDescription: {self.description}\nPrice: {self.price}")
    
class Order(models.Model):
    choices = [('Cash','Cash'),('Card','Card'),('Digital Wallet','Digital Wallet')]
    orderdatetime = models.DateTimeField(auto_now_add=True)
    paymentmode = models.CharField(choices=choices)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class OrderItem(models.Model):
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

