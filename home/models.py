from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=100,null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True),
    about_yourself = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Vehicle_Ads(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    company_name = models.CharField(max_length=122,null=True, blank=True)
    vehicle_name = models.CharField(max_length=122,null=True, blank=True)

    model = models.IntegerField()

    km_Driven = models.IntegerField()
    price = models.IntegerField()
    Description = models.TextField(max_length=5000)
    Condition_Choices = [("USED", "Used"), ("Brand New", "Brand New"),
                         ("Likely New", "Likely New"), ("Not Working", "Not Working")]
    Condition = models.CharField(choices=Condition_Choices, max_length=20)
    photo = models.ImageField()
    location= models.CharField(max_length=100,null=True, blank=True)
    additional_details = models.TextField(max_length=300, null=True, blank=True)


    def __str__(self):
        return self.vehicle_name

    @property
    def imageurl(self):
        try:
            url = self.photo.url
        except:
            url=''
        return url


class Mobile_and_Accessories_Ads(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=122,null=True, blank=True)
    model_name = models.CharField(max_length=122,null=True, blank=True)
    battery_health=models.CharField(max_length=2,null=True, blank=True)
    price = models.IntegerField()
    Description = models.TextField(max_length=5000)
    Condition_Choices = [("USED", "Used"), ("Brand New", "Brand New"),
                         ("Likely New", "Likely New"), ("Not Working", "Not Working")]
    Condition = models.CharField(choices=Condition_Choices, max_length=20)
    photo = models.ImageField()
    location = models.CharField(max_length=100,null=True, blank=True)
    additional_details = models.TextField(max_length=300, null=True, blank=True)
    def __str__(self):
        return self.brand




class Electronics_TVs_and_More_Ads(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=122,null=True, blank=True)
    price = models.IntegerField()
    Description = models.TextField(max_length=5000,null=True, blank=True)
    Condition_Choices = [("USED", "Used"), ("Brand New", "Brand New"),
                         ("Likely New", "Likely New"), ("Not Working", "Not Working")]
    Condition = models.CharField(choices=Condition_Choices, max_length=20)
    photo = models.ImageField()
    location = models.CharField(max_length=100,null=True, blank=True)
    additional_details = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title


class UserItem(models.Model):
    customer= models.ForeignKey(User, on_delete=models.CASCADE)
    vehicels_ad= models.ForeignKey(Vehicle_Ads, on_delete=models.CASCADE)
    mobiles_ad= models.ForeignKey(Mobile_and_Accessories_Ads, on_delete=models.CASCADE)
    electronics_ad= models.ForeignKey(Electronics_TVs_and_More_Ads, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)