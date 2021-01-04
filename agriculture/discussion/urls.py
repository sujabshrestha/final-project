from django.urls import path
from . views import feedback,displayforum,addInForum,addInDiscussion,reply
urlpatterns = [
    
    path('feedback/', feedback, name='feedback'),
    path('displayforum/',displayforum,name='displayforum'),
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
    path('reply/',reply,name='reply'),
 
    
]
