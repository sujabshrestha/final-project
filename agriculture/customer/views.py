from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from . forms import UserRegisterform,userloginform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Customer,Cancellation
from products.models import Order
from seller.models import Seller
from products.models import Product,Category
from discussion.models import Discussion, Reply
from django.core.paginator import Paginator
# Create your views here.
def home(request):  
    currentuser = request.user.username 
    if Seller.objects.filter(username=currentuser).exists():
        seller = 'yes'
    else:
        seller = None   
    allprods = [] 
    prod = Product.objects.all().order_by('-id')
    page = request.GET.get('page',1)
    paginator = Paginator(prod,12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:    
        products = paginator.page(paginator.num_pages)
    n = len(products)
    allprods.append([products,range(1,n)])

    mostorder = []
    mostp = [] 
    orderproduct = Order.objects.all()
    for o in orderproduct:
        pid = o.product_id
        mostp.append(pid)
    mp = list(set(mostp))
    
    mostprod = Product.objects.filter(id__in=mp).order_by('-id')
    page = request.GET.get('page',1)
    paginator = Paginator(mostprod,8)
    try:
        mostproducts = paginator.page(page)
    except PageNotAnInteger:
        mostproducts = paginator.page(1)
    except EmptyPage:    
        mostproducts = paginator.page(paginator.num_pages)
    m = len(mostproducts)
    mostorder.append([mostproducts,range(1,m)])
    context = {
        'seller':seller,
        'products': allprods,
        'mostorder':mostorder,
        

    }       
    return render(request,'customer/home.html', context)

def register(request):
    currentuser = request.user.username
    if Seller.objects.filter(username=currentuser).exists():
        seller = 'yes'
    else:
        seller = None
    if request.method == 'POST':
        form = UserRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            detail = Customer(username=username,firstname=firstname,lastname=lastname,email=email)
            detail.save()
            messages.success(request,'account created')
            return redirect('login')
    else:
        form = UserRegisterform()  
    context = {
        'seller':seller,
        'form' : form 
    }        
    return render(request,'customer/register.html', context)




def about(request):
    return render(request,'customer/about.html')


def Login(request):
    currentuser = request.user.username
    if Seller.objects.filter(username=currentuser).exists():
        seller = 'yes'
    else:
        seller = None
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            if Customer.objects.filter(username=username).exists():
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request,user)
                    return redirect('home')
                else:
                    messages.info(request, 'Username or Password is incorrect! Please enter valid username and password')
            else:
                messages.info(request, 'Please provide customer details to login!')
    form = userloginform()
    context = {
        'seller':seller,
        'form' : form
    }
    return render(request, 'customer/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def search(request):
    search_title = request.GET.get('search')
    if search_title == '':
        return render(request,'customer/noresults.html',{'query':search_title})
    else:    
        allposttitle = Product.objects.filter(title__icontains=search_title)
        allpostcontent = Product.objects.filter(content__icontains=search_title)
        allpost = allposttitle.union(allpostcontent)
    context={
        'products': allpost,
        'query':search_title
    }
    return render(request,'customer/search.html',context)


def changepassword(request):
    return render(request,'customer/changepassword.html')



def profile(request):
    currentuser = request.user.username
    profile = Customer.objects.filter(username=currentuser).first()
    allprods = [] 
    prod = Order.objects.filter(username=currentuser).order_by('-id')
    page = request.GET.get('page',1)
    paginator = Paginator(prod,10)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:    
        products = paginator.page(paginator.num_pages)
    n = len(products)
    allprods.append([products,range(1,n)])
    
    allcancels = [] 
    cprod = Cancellation.objects.filter(username=currentuser).order_by('-id')
    page = request.GET.get('page',1)
    paginator = Paginator(cprod,10)
    try:
        cproducts = paginator.page(page)
    except PageNotAnInteger:
        cproducts = paginator.page(1)
    except EmptyPage:    
        cproducts = paginator.page(paginator.num_pages)
    n = len(cproducts)
    allcancels.append([cproducts,range(1,n)])
    context = {
        'profile':profile,
        'allprods':allprods,
        'allcancels':allcancels
    }
    return render(request,'customer/profile.html',context)


# Create your views here.
def updateprofile(request):
    currentuser = request.user.username
    if Seller.objects.filter(username=currentuser).exists():
        seller = 'yes'
    else:
        seller = None
    details = Customer.objects.filter(username=currentuser).first()   
    context={
        'seller':seller,
        'details':details  
    }
    return render(request,'customer/updateprofile.html',context)

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
                Customer.objects.filter(username=currentuser).update(firstname=first_name,lastname=last_name, phone=phone, delivery=address)
                Order.objects.filter(username=currentuser).update(customer_contact=phone,delivery_address=address)
            else:
                messages.info(request, 'Enter valid Phone Number!')
                return redirect('updateprofile')
        else:
            messages.info(request, 'All fields are required!')
            return redirect('updateprofile')

        if image is not None and image != '':
            imagedetail = Customer.objects.get(username=currentuser)
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
            return redirect('profile')
            return redirect('profile')
        else:
            messages.info(request, 'Please insert an image!')
            return redirect('updateprofile')  


def ordercancel(request,od):
    currentuser = request.user.username 
    order = Order.objects.filter(ordernumber=od,username=currentuser).first()
    pname = order.product_name
    pqty = order.product_quantity
    pid = order.product_id
    pimage = order.image

    cancel = Cancellation(username=currentuser,product_name=pname,product_quantity=pqty,product_id=pid,image=pimage)
    csave = cancel.save()
    Order.objects.filter(ordernumber=od,username=currentuser).delete()
    return redirect('profile')