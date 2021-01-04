from django.db import models

# Create your models here.
class Seller(models.Model):
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.CharField(max_length=255,default='')
    image = models.ImageField(default='/profile_pics/default.jpg',upload_to='profile_pics')
    phone = models.IntegerField(default=0)
    address = models.CharField(default='',max_length=30)
