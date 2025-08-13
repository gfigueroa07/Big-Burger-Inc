import uuid
from django.db import models

class Item(models.Model):
    id = models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True)
    name = models.CharField(unique=True)
    category = models.CharField(unique=True, max_length=20)
    picture = models.ImageField(upload_to='item_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'items'
        
    def __str__(self):
        return self.name
    
# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    telephone_number = models.DecimalField(max_digits=10, decimal_places=2)
    verification_code = models.DecimalField(max_digits=4,  decimal_places=2)
    coupons = models.ManyToManyField('Coupon', through='CustomerCoupon')

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.name
    
class Coupon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    items_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=100)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    maximum_discount_value = models.DecimalField(max_digits=5, decimal_places=2)
    max_units_per_customer = models.IntegerField()
    single_use = models.BooleanField(default=True)
    needed_item_quantity_to_use = models.IntegerField(default=1)
    applicable_on_item_amount = models.IntegerField()

    class Meta:
        db_table = 'coupons'
        
    def __str__(self):
        return self.name
    

    
class CustomerCoupon(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    coupon = models.ForeignKey('Coupon', on_delete=models.CASCADE)
    acquired_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    used_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('customer', 'coupon')  # composite PK behavior
        db_table = 'customer_coupons'