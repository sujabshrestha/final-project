from django.contrib import admin
from .models import Feedback,Discussion,forum,Reply
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display =['Name','Email','Phone','Message']

admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Discussion)
admin.site.register(forum)
admin.site.register(Reply)