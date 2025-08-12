from django.contrib import admin
from .models import Items, Customers, Coupons, CustomerCoupon

# Register your models here.

admin.site.register([Items, Customers, Coupons, CustomerCoupon])