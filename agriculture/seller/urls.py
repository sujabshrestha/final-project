from django.urls import path
from . views import sellerregister,Login,logoutUser,sellerdashboard,update,updateproduct,delete,updateprof,profupdate
urlpatterns = [
    path('sellerregister/', sellerregister, name='sellerregister'),
    path('sellerlogin/', Login, name='sellerlogin'),
    path('logout/', logoutUser, name='logout'),
    path('dashboard/', sellerdashboard, name='sellerdashboard'),
    path('update/<int:pk>/', update, name='update'),
    path('updateproduct/<str:ph>/', updateproduct, name='updateproduct'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('updateprof/', updateprof, name='updateprof'),
    path('profupdate/', profupdate, name='profupdate'),

 
]
