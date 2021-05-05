from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Brands(models.Model):
    brand_name = models.TextField()
    no_of_products=models.IntegerField(default=0)

class Products(models.Model):
    product_name = models.TextField()
    product_type = models.TextField()
    product_price = models.IntegerField(default=0)
    product_image =models.ImageField(upload_to='media')

    brand = models.ForeignKey(Brands,on_delete=models.CASCADE, default="")
class Customer(models.Model):
    fname = models.TextField()
    lname = models.TextField(default=" ")
    address = models.TextField()
    email_id = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    products = models.ManyToManyField(Products)
    class Meta:
        ordering = ['fname']

