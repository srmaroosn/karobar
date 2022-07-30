from django.contrib import admin
from django.urls import path
from django.views import View
from . import views 


urlpatterns = [
    path('',views.index, name ='index'),
    path('createads/', views.create_Ads, name='createads'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('adssingleview/', views.adssingleview, name='adssingleview'),
    path('electronics/', views.electronics, name='electronics'),
    path('login/', views.login, name='login'),
    path('mobile/', views.mobile, name='mobile'),
    path('register/', views.register, name='register'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('myads/', views.myads, name='myads')




    
]