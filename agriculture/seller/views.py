from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from customer.forms import UserRegisterform,userloginform,SellerRegisterform
from .models import Seller
from django.contrib.auth.models import User
from products.models import Product,Category
from discussion.models import Discussion, Reply
from django.contrib import messages

# Create your views here.
def sellerregister(request):
    currentuser = request.user.username
    if Seller.objects.filter(username=currentuser).exists():
        seller = 'yes'
    else:
        seller = None   
    if request.method == 'POST':
        form = SellerRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            detail = Seller(username=username,firstname=firstname,lastname=lastname,email=email,phone=phone,address=address)
            detail.save()
            messages.success(request,'account created')
            return redirect('sellerlogin')
    else:
        form = SellerRegisterform()    
    context = {
        'seller':seller,
        'form' : form 
    }    
    return render(request,'seller/register.html', context)

def Login(request):   
    currentuser = request.user.username
    if Seller.objects.filter(username=currentuser).exists():
        seller = 'yes'
    else:
        seller = None
    if request.user.is_authenticated:
        logout(request)
        return redirect('sellerlogin')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            if Seller.objects.filter(username=username).exists():
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('home')
                else:
                    messages.info(request, 'Username or Password is incorrect! Please enter valid username and password')
            else:
                messages.info(request, 'Provide supplierdetails to login!')
       
        form = userloginform()
        
    context = {
        'seller':seller,
        'form' : form
    }
    return render(request, 'seller/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def sellerdashboard(request):
    currentuser = request.user.username    
    if Seller.objects.filter(username=currentuser).exists():
        seller = 'yes'
    else:
        seller = None
    product = Product.objects.filter(author = currentuser) 
    sellers = Seller.objects.filter(username=currentuser).first()
    context = {
        'seller':seller,
        'product':product,
        'sellers':sellers
    }
    return render(request, 'seller/dashboard.html', context)   

def updateprof(request):
    currentuser = request.user.username
    if Seller.objects.filter(username=currentuser).exists():
        seller = 'yes'
    else:
        seller = None
    details = Seller.objects.filter(username=currentuser).first()   
    context={
        'seller':seller,
        'details': details
        
    }
    return render(request,'seller/updateprofile.html',context)

def profupdate(request):
    currentuser = request.user.username   
    if request.method=='POST':    
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        if first_name != '' and last_name != '' and phone != '' and address != '':
            if len(phone) == 10:
                User.objects.filter(username=currentuser).update(first_name=first_name,last_name=last_name)
                Seller.objects.filter(username=currentuser).update(firstname=first_name,lastname=last_name, phone=phone, address=address)
            else:
                messages.info(request, 'Enter valid Phone Number!')
                return redirect('updateprof')
        else:
            messages.info(request, 'All fields are required!')
            return redirect('updateprof')

        if image is not None and image != '':
            imagedetail = Seller.objects.get(username=currentuser)
            imagedetail.image = request.FILES.get('image')
            imagedetail.save()
            imagedetail1 = Discussion.objects.filter(username=currentuser)
            for i in imagedetail1:
                i.image = request.FILES.get('image')
                i.save()
            imagedetail2 = Reply.objects.filter(username=currentuser)
            for i in imagedetail2:
                i.image = request.FILES.get('image')
                i.save()
            return redirect('sellerdashboard')
        else:
            messages.info(request, 'Please insert an image!')
            return redirect('updateprof')   


def update(request,pk):
    currentuser = request.user.username    
    if Seller.objects.filter(username=currentuser).exists():
        seller = 'yes'
    else:
        seller = None
    product = Product.objects.filter(id=pk).first() 
    category = Category.objects.all()
    context = {
        'seller':seller,
        'product':product,
        'category':category
    }
    return render(request, 'seller/update.html', context)   
 
def updateproduct(request,ph):
    currentuser = request.user.username     
    if request.method == 'POST':
        title = request.POST.get('title') 
        p_type = request.POST.get('p_type') 
        content = request.POST.get('content')
        image = request.FILES.get('image')
        area = request.POST.get('area')
        soilfertility = request.POST.get('soilfertility')
        growingperiod = request.POST.get('growingperiod')
        climate = request.POST.get('climate')
        composition = request.POST.get('composition')
        print(composition)
        benifits = request.POST.get('benifits')
        healthbenifits = request.POST.get('healthbenifits')
        category = request.POST.get('category')
        price = request.POST.get('price')
        ctitle = title.capitalize()
        if category == 'vegetable(seed)':
            if ctitle != '':
                if Product.objects.exclude(id=ph).filter(title=ctitle).exists():
                    messages.info(request,'Same product name available add different product name!!')
                    return redirect('/seller/update/' +ph+ '/')
                else:
                    if p_type != '':
                        if content != '':
                            if area != '':
                                if growingperiod != '':
                                    if climate != '':
                                        if healthbenifits != '':
                                            if image != '' and image is not None:

                                                detail = Product.objects.filter(id=ph).update(title=title,content=content,price=price,author=currentuser,p_type=p_type,growingperiod=growingperiod,climate=climate,p_area=area,soilfertility=soilfertility,healthbenifits=healthbenifits)
                                                imagedetail = Product.objects.get(id=ph)
                                                imagedetail.image = request.FILES.get('image')
                                                imagedetail.save()
                                                messages.info(request, 'Updated Successfully')
                                                return redirect('sellerdashboard')
                                            else:
                                                messages.info(request,'insert image')
                                                return redirect('/seller/update/' +ph+ '/')


                                        else:
                                            messages.info(request,'please define Healthbenifits')
                                            return redirect('/seller/update/' +ph+ '/')
                                    else:
                                        messages.info(request,'please define climate')
                                        return redirect('/seller/update/' +ph+ '/')


                                else:
                                    messages.info(request,'please define grwoingperiod')
                                    return redirect('/seller/update/' +ph+ '/')

                            else:
                                messages.info(request,'please define content')
                                return redirect('/seller/update/' +ph+ '/')


                        else:
                            messages.info(request,'please define content')
                            return redirect('/seller/update/' +ph+ '/')   


                    else: 
                        messages.info(request,'please define type')
                        return redirect('/seller/update/' +ph+ '/') 
            else:
                messages.info(request,'please provide title')
                return redirect('/seller/update/' +ph+ '/')
        else:
            if ctitle != '':
                if Product.objects.exclude(id=ph).filter(title=ctitle).exists():
                    messages.info(request,'Same product name available add different product name!!')
                    return redirect('/seller/update/' +ph+ '/')
                else:
                    if p_type != '':
                        if composition != '':
                            if benifits != '':
                                if content != '':
                                    if image != '' and image is not None:

                                        detail = Product.objects.filter(id=ph).update(title=title,content=content,price=price,author=currentuser,p_type=p_type,benifits=benifits,fcomposition=composition)
                                        imagedetail = Product.objects.get(id=ph)
                                        imagedetail.image = request.FILES.get('image')
                                        imagedetail.save()
                                        messages.info(request, 'Updated Successfully')
                                        return redirect('sellerdashboard')
                                    else:
                                        messages.info(request,'insert image')
                                        return redirect('/seller/update/' +ph+ '/')
                                else:
                                    messages.info(request,'add content!!')
                                    return redirect('/seller/update/' +ph+ '/')

                            else:
                                messages.info(request,'add benefits!!')
                                return redirect('/seller/update/' +ph+ '/')
                        else:
                            messages.info(request,'add composition!!')
                            return redirect('/seller/update/' +ph+ '/')

                    else:
                        messages.info(request,'add type!!')
                        return redirect('/seller/update/' +ph+ '/')
            else:
                messages.info(request,'please provide title')
                return redirect('/seller/update/' +ph+ '/')            
    return HttpResponse()


def delete(request,pk):
    currentuser = request.user.username    
    Product.objects.filter(id=pk).delete()
    return redirect('sellerdashboard')
    