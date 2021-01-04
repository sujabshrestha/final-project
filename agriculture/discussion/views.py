from django.shortcuts import render,redirect
from .models import Feedback,Reply,Discussion,forum
from seller.models import Seller
from customer.models import Customer
from django.contrib import messages
from products.models import Product 
from django.contrib.auth.decorators import login_required

# Create your views here.
def feedback(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        detail = Feedback(Name=name,Phone=phone,Email=email,Message=message)
        detail.save()
        messages.success(request, 'Thanks for your words!!' )
        return redirect('feedback')
    return render(request,'discussion/feedback.html')

from .models import * 
from .forms import * 
# Create your views here.
@login_required(login_url='login')
def displayforum(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions =Discussion.objects.all() 
    reply =Reply.objects.all() 
    context={'forums':forums,
              'count':count,
              'discussions':discussions,
              'reply':reply}
    return render(request,'discussion/displayforum.html',context)

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/discussion/displayforum')
    context ={'form':form}
    return render(request,'discussion/addInForum.html',context)

def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        username = request.user.username
        discuss = request.POST.get('discuss')
        if Seller.objects.filter(username=username).exists():
            profile = Seller.objects.filter(username=username).first()
            image = profile.image
            d = Discussion(username=username,discuss=discuss,image=image)
            d.save()
            return redirect('/discussion/displayforum')
        else:
            profile = Customer.objects.filter(username=username).first()
            image = profile.image
            d = Discussion(username=username,discuss=discuss,image=image)
            d.save()
            return redirect('/discussion/displayforum')
                
    context ={'form':form}
    return render(request,'discussion/addInDiscussion.html',context)

def reply(request):
    if request.method == 'POST':
        username = request.user.username
        reply = request.POST.get('reply')
        duserid = request.POST.get('duserid')
        if Seller.objects.filter(username=username).exists():
            profile = Seller.objects.filter(username=username).first()
            image = profile.image
            d = Reply(username=username,discuss_userid=duserid,image=image,reply=reply)
            d.save()
            return redirect('/discussion/displayforum')
        else:
            profile = Customer.objects.filter(username=username).first()
            image = profile.image
            d = Reply(username=username,discuss_userid=duserid,image=image,reply=reply)
            d.save()
            return redirect('/discussion/displayforum')
                
  
