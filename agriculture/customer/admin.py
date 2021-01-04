from django.contrib import admin


# Register your models here.
from . models import Customer,Cancellation

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username','firstname','lastname','email']

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Cancellation)