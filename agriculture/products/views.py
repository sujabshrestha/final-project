from django.shortcuts import render,redirect
from .models import Product,Category,Order,Review
from customer.models import Customer
from seller.models import Seller
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from django.core.paginator import Paginator
from django.core import mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from agriculture.settings import EMAIL_HOST_USER
# Create your views here.

def displayproduct(request):
    currentuser = request.user.username
    if Seller.objects.filter(username=currentuser).exists():
        seller = 'yes'
    else:
        seller = None
    
    products = Product.objects.all()
    context = { 
        'seller':seller,
        'products' :products

    }
    return render(request,'products/displayproduct.html', context)

def addproduct(request):
    currentuser = request.user.username
    if Seller.objects.filter(username=currentuser).exists():
        seller = 'yes'
    else:
        seller = None
    category = Category.objects.all()
    
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
        benifits = request.POST.get('benifits')
        healthbenifits = request.POST.get('healthbenifits')
        category = request.POST.get('category')
        price = request.POST.get('price')
        ctitle = title.capitalize()
        if category == 'vegetable(seed)':
            if ctitle != '':
                if Product.objects.filter(title=ctitle).exists():
                    messages.info(request,'Same product name available add different product name!!')
                    return redirect('addproduct')
                else:
                    if p_type != '':
                        if content != '':
                            if area != '':
                                if growingperiod != '':
                                    if climate != '':
                                        if healthbenifits != '':
                                            if image != '' and image is not None:
                                                detail = Product(title=title,content=content,image=image,price=price,author=currentuser,category=category,p_type=p_type,growingperiod=growingperiod,climate=climate,p_area=area,soilfertility=soilfertility,healthbenifits=healthbenifits)
                                                detail.save() 
                                                messages.info(request,'product added successfully!')
                                                return redirect('sellerdashboard')
                                            else:
                                                messages.info(request,'insert image')
                                                return redirect('addproduct')


                                        else:
                                            messages.info(request,'please define Healthbenifits')
                                            return redirect('addproduct')

                                    else:
                                        messages.info(request,'please define climate')
                                        return redirect('addproduct')


                                else:
                                    messages.info(request,'please define grwoingperiod')
                                    return redirect('addproduct')

                            else:
                                messages.info(request,'please define content')
                                return redirect('addproduct')


                        else:
                            messages.info(request,'please define content')
                            return redirect('addproduct')    


                    else: 
                        messages.info(request,'please define type')
                        return redirect('addproduct')     
            else:
                messages.info(request,'please provide title')
                return redirect('addproduct')   
        else:
             if ctitle != '':
                if Product.objects.filter(title=ctitle).exists():
                    messages.info(request,'Same product name available add different product name!!')
                    return redirect('addproduct')
                else:
                    if p_type != '':
                        if composition != '':
                            if benifits != '':
                                if content != '':
                                    if image != '' and image is not None:
                                        detail = Product(title=title,content=content,image=image,price=price,author=currentuser,category=category,p_type=p_type,benifits=benifits,fcomposition=composition)
                                        detail.save() 
                                        messages.info(request,'product added successfully!')
                                        return redirect('sellerdashboard')
                                    else:
                                        messages.info(request,'insert image')
                                        return redirect('addproduct')
                                else:
                                    messages.info(request,'add content!!')
                                    return redirect('addproduct')


                            else:
                                messages.info(request,'add composition!!')
                                return redirect('addproduct')



                        else:
                            messages.info(request,'add composition!!')
                            return redirect('addproduct')


                    else:
                        messages.info(request,'add type!!')
                        return redirect('addproduct')

    context = { 
        'seller':seller,
        'category':category
       
    }    
    return render(request,'products/addproduct.html',context)



@login_required(login_url='login')
def orderdashboard(request,pk):
    currentuser = request.user.username
    if Customer.objects.filter(username=currentuser).exists():
        orderproducts = Product.objects.filter(id=pk).first()
        allreviews = [] 
        review = Review.objects.filter(product_id=pk).order_by('-id')
        page = request.GET.get('page',1)
        paginator = Paginator(review,8)
        try:
            reviews = paginator.page(page)
        except PageNotAnInteger:
            reviews = paginator.page(1)
        except EmptyPage:    
            reviews = paginator.page(paginator.num_pages)
        n = len(reviews)
        allreviews.append([reviews,range(1,n)])

        prod = Product.objects.filter(id=pk).first()
        cat = prod.category
        allprod = Product.objects.filter(category=cat).exclude(id=pk)
        context ={
            'product' : orderproducts,
            'allreviews':allreviews,
            'allprod':allprod


        }
        return render(request,'products/order.html',context)
    else:
        messages.info(request,'Please login as Customer to order!')
        return redirect('login')    



@login_required(login_url='login')
def orderdetail(request,pk):
    currentuser = request.user.username
    if Seller.objects.filter(username=currentuser).exists():
        seller = 'yes'
    else:
        seller = None
    orderproducts = Product.objects.filter(id=pk).first()
 
    context ={
        'seller':seller,
        'product' : orderproducts,
        
     
    }
    return render(request,'products/detail.html',context)    


@login_required(login_url='login')
def proceedorder(request):
    currentuser = request.user.username
    if request.method == 'POST':
        prodid = request.POST.get('prodid')
        packet = request.POST.get('packet')
        price = request.POST.get('price')

        product = Product.objects.filter(id=prodid).first()
        prodname = product.title
        customer = Customer.objects.filter(username=currentuser).first()
        context = {
            'prodid':prodid,
            'packet':packet,
            'price':price,
            'prodname':prodname,
            'customer': customer
        } 
        return render(request,'products/proceedorder.html', context)   
    else:
        return redirect('home')    


def proceed(request):
    currentuser = request.user.username
    if request.method == 'POST':
        delivery = request.POST.get('deliveryaddress')
        phone = request.POST.get('phone')
        prodid = request.POST.get('prodid')
        packet = request.POST.get('packet')
        price = request.POST.get('price')
        totalprice = request.POST.get('total')
        product = Product.objects.filter(id=prodid).first()
        prodname = product.title
        Customer.objects.filter(username=currentuser).update(delivery=delivery,phone=phone)
        detail = Customer.objects.filter(username=currentuser).first()
        
    
        context = {
            'prodid':prodid,
            'packet':packet,
            'price':price,
            'prodname':prodname,
            'totalprice':totalprice,
            'detail':detail
        } 
        return render(request,'products/proceed.html', context) 
    else:
        return redirect('home')
           
def order(request):
    currentuser = request.user.username
    
    if request.method == 'POST':
        ordernumber = random.randint(11111111,99999999)
        request.session['ordernumber'] = ordernumber
        prodid = request.POST.get('prodid')
        packet = request.POST.get('packet') + 'packet'
        price = request.POST.get('price')
        totalprice = request.POST.get('total')
        product = Product.objects.filter(id=prodid).first()
        prodname = product.title
        prodcat = product.category
        prodimage = product.image
        sellerid = product.author
        seller = Seller.objects.filter(username=sellerid).first()
        seller_email = seller.email

        detail = Customer.objects.filter(username=currentuser).first()
        u_email = detail.email
        u_contact = detail.phone
        u_delivery = detail.delivery 
        delivery_charge = 100
        
        order_d = Order(username=currentuser,user_email=u_email,image=prodimage,customer_contact=u_contact,product_name=prodname,product_id=prodid,product_quantity=packet,product_category=prodcat,subtotal=price,delivery_charge=delivery_charge,total_amount=totalprice,delivery_address=u_delivery,ordernumber=ordernumber)  
        order_d.save()
        orderp = Order.objects.filter(username=currentuser,ordernumber=ordernumber).first()
        mail_subject = 'New Order'
        html_message = render_to_string('products/ordermail.html', {
            'orderp': orderp,

            })
        plain_message = strip_tags(html_message)
        from_email = EMAIL_HOST_USER
        to = seller_email
        mail.send_mail(mail_subject, plain_message, from_email, [to], fail_silently=False, html_message=html_message)

        mail_subject1 = 'Order Placed Successfully'
        html_message1 = render_to_string('products/ordermail_customer.html', {
            'orderp': orderp,

            })
        plain_message1 = strip_tags(html_message1)
        from_email1 = EMAIL_HOST_USER
        to1 = u_email
        mail.send_mail(mail_subject1, plain_message1, from_email1, [to1], fail_silently=False, html_message=html_message1)      
    return redirect('confirm')       


def confirm(request):
    currentuser = request.user.username
    ordernumber = request.session['ordernumber']
    context={
        'ordernumber':ordernumber,
    }
    return render(request,'products/confirmorder.html', context) 


def filterproducts(request,cat):
    products = Product.objects.filter(category=cat)
    context={
        'products':products,
        'cat':cat
    }
    return render(request,'products/displayproduct.html',context) 

def allprod(request):
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
    print(n)
    allprods.append([products,range(1,n)])

    context={
        'products':allprods
    }
    return render(request,'products/allprods.html',context)

def ordertracker(request):
    if request.method == 'POST':
        ordernumber = request.POST.get('ordernumber')
        if Order.objects.filter(ordernumber=ordernumber).exists():
            order = Order.objects.filter(ordernumber=ordernumber).first()
            n = 1
            context={
                'order':order,
                'len':n
            }
            return render(request,'products/ordertracker.html',context) 
        else:
            messages.info(request,'There is no order available for this order number')
            n=0
            context={
                'len':n
            }
            return render(request,'products/ordertracker.html',context) 
    else:
        return redirect('home')


def review(request):
    currentuser = request.user.username
    if request.method == 'POST':
        username = currentuser
        productid = request.POST.get('productid')
        review = request.POST.get('review')
        profile = Customer.objects.filter(username=currentuser).first()
        image = profile.image
        review_save = Review(product_id=productid,review=review,image=image,username=username)
        review_save.save()
        return redirect('/products/orderdashboard/' +productid+ '/')


def compareproduct(request):
    if 'pid' in request.session: 
        pid = request.session['pid']   
        phk = request.session['phk']   
        product1 = Product.objects.filter(id=pid).first()
        product2 = Product.objects.filter(id=phk).first()
        del request.session['pid']
        del request.session['phk']
        request.session.modified=True
        context={     
            'product1':product1,
            'product2':product2,
        }
        return render(request,'products/productcompare.html',context)


    else:
        return redirect('home')
   
   

def compare(request,pid,phk):
    request.session['pid']=pid
    request.session['phk']=phk
    return redirect('compareproduct')


def payment(request):
    return render(request,'products/payment.html')