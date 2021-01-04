from django.contrib import admin
from .models import Product,Category,Order,Review
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','p_type','p_area','growingperiod','climate','soilfertility','image','date_posted','author','category'] 

class OrderAdmin(admin.ModelAdmin):
    list_display = ['ordernumber','username','user_email','customer_contact','delivery_address','product_name','product_id','product_quantity','subtotal','delivery_charge','total_amount','date_posted','paymentmethod','paymentstatus','orderstatus'] 

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Order,OrderAdmin)
admin.site.register(Review)