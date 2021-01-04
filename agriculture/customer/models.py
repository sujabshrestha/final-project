from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.CharField(max_length=255,default='')
    delivery = models.CharField(max_length=255,default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(default='/profile_pics/default.jpg',upload_to='profile_pics')

    # pic,phone,add

class Cancellation(models.Model):            
    username = models.CharField(max_length=30)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    product_name = models.CharField(max_length=255)
    product_id = models.IntegerField()
    product_quantity = models.CharField(max_length=255)    