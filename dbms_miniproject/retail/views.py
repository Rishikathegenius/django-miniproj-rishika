from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from getpass import getpass
from .models import Brands,Products,Customer
def index(request):
   return render(request, "index.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect("inside") 
        else:
            messages.info(request,'invalid credentials')
            return redirect("login")
    else:
        return render(request,'login.html') 

def inside(request):
   return render(request,'insideindex.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username taken.')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email taken.')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching.')
        return redirect('/')
    else:
        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')


def customers(request):
   #cust=Customer.objects.all()
   cust=Customer.objects.raw('SELECT * FROM retail_customer')
   pros=[]
   for cus in cust:
      c=cus.products.all()
      pros.append(c) 
   myfile = zip(cust, pros)
   context = {
      'myfile':myfile,
   }
   return render(request,'customers.html',context)
def addcustomers(request):
   if request.method == 'POST':
      fname = request.POST['fname']
      lname = request.POST['lname']
      address = request.POST['address']
      email_id = request.POST['email_id']
      phone = request.POST['phone']
      productname = request.POST['productname']
      if Customer.objects.filter(fname=fname).filter(lname=lname).exists():
         cust = Customer.objects.raw('SELECT * FROM retail_customer WHERE fname=%s',[fname])[0] 
         p1=Products.objects.raw('SELECT * FROM retail_products WHERE product_name=%s',[productname])[0]
         cust.products.add(p1)
         cust.save()
      else:
         cust = Customer()
         cust.fname=fname
         cust.lname=lname
         cust.address=address
         cust.email_id=email_id
         cust.phone=phone
         cust.save()
         #p1=Products.objects.get(product_name=productname)
         p1=Products.objects.raw('SELECT * FROM retail_products WHERE product_name=%s', [productname])[0]
         cust.products.add(p1)
         cust.save()
      return redirect("inside")
   return render(request,'addcustomers.html')
def product(request):
   prod=Products.objects.raw('SELECT * FROM retail_products')
   brandinthis = []
   for pr in prod:
      brandinthis.append(pr.brand)
   myfile = zip(prod, brandinthis)
   context = {
      'myfile':myfile,
   }
   return render(request,'product.html',context)
def addproduct(request):
   if request.method == 'POST':
      productname = request.POST['productname']
      producttype = request.POST['producttype']
      productprice = request.POST['productprice']
      brandname = request.POST['brandname']
      pro=Products()
      pro.product_name=productname
      pro.product_type=producttype
      pro.product_price=productprice
      pro.brand=Brands.objects.get(brand_name=brandname)
      pro.save()
      brandinthis = Brands.objects.get(brand_name=brandname)
      brandinthis.no_of_products+=1
      brandinthis.save()
      return redirect("inside")
   return render(request,'addproduct.html')
def addproduct1(request):
   if request.method == 'POST':
      productname = request.POST['productname']
      producttype = request.POST['producttype']
      productprice = request.POST['productprice']
      brandname = request.POST['brandname']
      pro=Products()
      pro.product_name=productname
      pro.product_type=producttype
      pro.product_price=productprice
      pro.brand=Brands.objects.get(brand_name=brandname)
      pro.save()
      brandinthis = Brands.objects.get(brand_name=brandname)
      brandinthis.no_of_products+=1
      brandinthis.save()
      return redirect("inside")
   return render(request,'addproduct1.html')
def addproduct2(request):
   if request.method == 'POST':
      productname = request.POST['productname']
      producttype = request.POST['producttype']
      productprice = request.POST['productprice']
      brandname = request.POST['brandname']
      pro=Products()
      pro.product_name=productname
      pro.product_type=producttype
      pro.product_price=productprice
      pro.brand=Brands.objects.get(brand_name=brandname)
      pro.save()
      brandinthis = Brands.objects.get(brand_name=brandname)
      brandinthis.no_of_products+=1
      brandinthis.save()
      return redirect("inside")
   return render(request,'addproduct2.html')
def addproduct3(request):
   if request.method == 'POST':
      productname = request.POST['productname']
      producttype = request.POST['producttype']
      productprice = request.POST['productprice']
      brandname = request.POST['brandname']
      pro=Products()
      pro.product_name=productname
      pro.product_type=producttype
      pro.product_price=productprice
      pro.brand=Brands.objects.get(brand_name=brandname)
      pro.save()
      brandinthis = Brands.objects.get(brand_name=brandname)
      brandinthis.no_of_products+=1
      brandinthis.save()
      return redirect("inside")
   return render(request,'addproduct3.html')
def brand(request):
   brandswehave=Brands.objects.raw('SELECT * FROM retail_brands')
   context = {
      'brandswehave':brandswehave,
   }
   return render(request,'brand.html',context)
def addbrand(request):
   if request.method == 'POST':
      brandname = request.POST['brandname']
      br = Brands()
      br.brand_name=brandname
      br.save()
      return redirect("inside")
   return render(request,'addbrand.html')
def addbrand1(request):
   if request.method == 'POST':
      brandname = request.POST['brandname']
      br = Brands()
      br.brand_name=brandname
      br.save()
      return redirect("inside")
   return render(request,'addbrand1.html')
def addbrand2(request):
   if request.method == 'POST':
      brandname = request.POST['brandname']
      br = Brands()
      br.brand_name=brandname
      br.save()
      return redirect("inside")
   return render(request,'addbrand2.html')
def addbrand3(request):
   if request.method == 'POST':
      brandname = request.POST['brandname']
      br = Brands()
      br.brand_name=brandname
      br.save()
      return redirect("inside")
   return render(request,'addbrand3.html')