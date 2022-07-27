from django.contrib import admin

# Register your models here.
from .models import*
admin.site.register(Customer)
admin.site.register(Vehicle_Ads)
admin.site.register(Mobile_and_Accessories_Ads)
admin.site.register(Electronics_TVs_and_More_Ads)
admin.site.register(UserItem)
