from django.urls import path
from . views import home,about,register,Login,logoutUser,search,changepassword,profile,updateprofile,profupdate,ordercancel
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('login/', Login, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('search/', search, name='search'),
    path('changepassword/', changepassword, name='changepassword'),
    path('profile/',profile,name='profile'),
    path('updateprofile/', updateprofile, name='updateprofile'),
    path('profupdate/', profupdate, name='profupdate'),
    path('ordercancel/<str:od>/', ordercancel, name='ordercancel'),
]
