from . forms import *
from . models import *
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,  logout
from django.contrib import messages
from django.contrib.auth import login as auth_login

def create_Ads(request):
#    if request.method =="POST":
    # title = request.POST['title']
 return render(request,'add_listing.html',)

def aboutus (request):
    return render(request,'aboutus.html')

def index (request):
    return render(request,'index.html')

def adssingleview (request):
    return render(request,'ads_single_view.html')

def dashboard (request):
    return render(request,'dashboard.html')

def electronics (request):
    return render(request,'electonics_category.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print("is this running")
            return redirect('index')
        else:
            messages.warning(request, "The information is not correct")
    
    return render(request,'login.html',context={})
    

def mobile(request):
    return render(request, 'mobile_category.html')

def register(request):
    if request.method =="GET":
        form= UserCreation()
        context={'form':form}
        return render(request, 'register.html', context)

    else:
        form=UserCreation(request.POST)
        if form.is_valid():
            user=form.save() 
            Customer.objects.create(user=user)

            
            return redirect('login')
    return render(request, 'register.html', context={'form':form}) 
    

def vehicles(request):
    vehicle=Vehicle_Ads.objects.all()
    context= {"vehicle":vehicle}
    return render (request, 'vehicle_category.html', context)


def user_logout(request):
    logout(request)
    
    return redirect('index')