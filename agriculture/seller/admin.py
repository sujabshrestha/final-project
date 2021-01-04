from django.contrib import admin
from .models import Seller
# Register your models here.
class SellerAdmin(admin.ModelAdmin):
    list_display = ['username','firstname','lastname','email','phone','address']

admin.site.register(Seller,SellerAdmin)