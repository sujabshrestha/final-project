from django.urls import path
from .views import (displayproduct,
addproduct,orderdashboard,orderdetail,
proceedorder,proceed,confirm,order,filterproducts,ordertracker,review,compareproduct,allprod,compare,payment)
urlpatterns = [
   path('displayproduct/',displayproduct,name='displayproduct'),
   path('addproduct/',addproduct,name='addproduct'),
   path('orderdashboard/<int:pk>/',orderdashboard,name='orderdashboard'),
   path('orderdetail/<int:pk>/',orderdetail,name='orderdetail'),
   path('proceedorder/',proceedorder,name='proceedorder'),
   path('proceed/',proceed,name='proceed'),
   path('payment/',payment,name='payment'),
   path('confirm/',confirm,name='confirm'),
   path('order/',order,name='order'),
   path('ordertracker/',ordertracker,name='ordertracker'),
   path('filterproduct/<str:cat>/',filterproducts,name='filterproducts'),
   path('review/',review,name='review'),
   path('allprods/',allprod,name='allprods'),
   path('compareproduct/',compareproduct,name='compareproduct'),
   path('compare/<int:pid>/<int:phk>/',compare,name='compare'),


 
]
