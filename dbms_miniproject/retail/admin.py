from django.contrib import admin
from .models import Customer,Products,Brands
# Register your models here.
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Brands)
