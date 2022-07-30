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
    
    
    details = Customer.objects.all()
  


    customer=request.user.customer
    form=CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    description= Customer.objects.all()
    print(description)
    
    return render(request, 'dashboard.html', context={ 'description':description, 'form':form, })
    

def electronics (request):
    electronic=Electronics_TVs_and_More_Ads.objects.all()
    context={'electronic':electronic}
    return render(request,'electonics_category.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('index')

        
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
    mobile=Mobile_and_Accessories_Ads.objects.all()
    context={'mobile':mobile}
    return render(request,'mobile_category.html', context)
    

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
def userprofile(request):
    customer=request.user.customer
    form=CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    return render(request, 'userprofile.html', context={'form':form})

def myads(request):
    orders = request.user.customer.vehicle_ads_set.all()
    return render(request, 'dashboard_my_ads.html', context={'orders':orders})