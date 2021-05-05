from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('inside', views.inside, name='inside'),
    path('product', views.product, name='product'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('addproduct1', views.addproduct1, name='addproduct1'),
    path('addproduct2', views.addproduct2, name='addproduct2'),
    path('addproduct3', views.addproduct3, name='addproduct3'),
    path('customers', views.customers, name='customers'),
    path('addcustomers', views.addcustomers, name='addcustomers'),
    path('brand', views.brand, name='brand'),
    path('addbrand', views.addbrand, name='addbrand'),
    path('addbrand1', views.addbrand1, name='addbrand1'),
    path('addbrand2', views.addbrand2, name='addbrand2'),
    path('addbrand3', views.addbrand3, name='addbrand3'),
    ]