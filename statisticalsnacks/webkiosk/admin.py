from django.contrib import admin
from .models import Customer, Address

admin.site.register((Customer, Address))
