from django.contrib import admin
from .models import Item, Customer, Coupon, CustomerCoupon

# Register your models here.

admin.site.register([Item, Customer, Coupon, CustomerCoupon])