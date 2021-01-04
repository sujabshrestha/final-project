from django.db import models
from PIL import Image
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    title = models.CharField(max_length=30)
    p_type = models.CharField(max_length=900,default='')
    p_area = models.CharField(max_length=900,default='',blank=True)
    growingperiod = models.CharField(max_length=900,default='',blank=True)
    climate = models.CharField(max_length=900,default='',blank=True)
    soilfertility = models.CharField(max_length=900,default='',blank=True)
    healthbenifits = models.TextField(max_length=2000,default='',blank=True)
    benifits = models.TextField(max_length=2000,default='',blank=True)
    content = models.TextField()
    fcomposition = models.CharField(max_length=1000,default='',blank=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics',blank=False)
    date_posted = models.DateTimeField(default=timezone.now,null=True)
    category = models.CharField(max_length=30,default='')
    price = models.IntegerField()
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',kwargs = {'pk':self.pk })


class Order(models.Model):
    STATUS = (
        ('processing','processing'),
        ('shipping','shipping'),
        ('delivered','delivered'),
    )
    PAYMENT = (
        ('pending','pending'),
        ('paid','paid'),
    )
    
    username = models.CharField(max_length=30)
    user_email = models.CharField(max_length=255)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    date_posted = models.DateTimeField(default=timezone.now,null=True)
    customer_contact = models.IntegerField()
    delivery_address= models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_id = models.IntegerField()
    product_quantity = models.CharField(max_length=255)
    product_category = models.CharField(max_length=255, default='')
    subtotal = models.IntegerField()
    delivery_charge = models.IntegerField()
    total_amount = models.IntegerField()
    ordernumber = models.IntegerField(default=0)
    orderstatus=models.CharField(max_length=255,default='processing',choices=STATUS)
    paymentmethod = models.CharField(max_length=255,default='cash on delivery')
    paymentstatus = models.CharField(max_length=255,default='pending',choices=PAYMENT)



class Review(models.Model):    
    username = models.CharField(max_length=30)
    date_posted = models.DateTimeField(default=timezone.now,null=True)
    product_id = models.IntegerField()
    review = models.CharField(max_length=2038)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics',null=True)