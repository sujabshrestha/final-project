from django.db import models
from django.utils import timezone

# Create your models here.
class Feedback(models.Model):
    Name = models.CharField(max_length=30,default='')
    Email = models.EmailField()
    Phone = models.IntegerField()
    Message = models.TextField()
    
#parent model
class forum(models.Model):
    CATEGORY = (
        ('vegetable seeds','vegetable seeds'),
        ('fertilizers','fertilizers'),     
    
    )
    name=models.CharField(max_length=200,default="anonymous",blank=True )
    email=models.CharField(max_length=200,blank=True,default='')
    topic= models.CharField(max_length=300)
    description = models.CharField(max_length=1000,blank=True)
    link = models.CharField(max_length=100 ,blank =True,default='')
    date_created=models.DateTimeField(default=timezone.now,null=True)
    category = models.CharField(max_length=255,default='',choices=CATEGORY)
    
    def __str__(self):
        return str(self.topic)

#child model
class Discussion(models.Model):
    discuss = models.CharField(max_length=1000,blank=True,default='')
    username = models.CharField(max_length=30,default='')
    date_posted = models.DateTimeField(default=timezone.now,null=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics',null=True)

    def __str__(self):
        return str(self.discuss)



class Reply(models.Model):
    reply = models.CharField(max_length=1000,blank=True,default='')
    username = models.CharField(max_length=30,default='')
    discuss_userid = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now,null=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics',null=True)

    def __str__(self):
        return str(self.reply)






