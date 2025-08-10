from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    telephone_number = models.DecimalField(max_digits=10, decimal_places=2)
    verification_code = models.DecimalField(max_digits=4,  decimal_places=2)

    def __str__(self):
        return self.name

class Items(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True)
    name = models.CharField(unique=True)
    category = models.CharField(unique=True, max_length=20)
    picture = models.ImageField(upload_to='item_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Coupons(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True)
    items_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    discount_percentage = models.IntegerField() 
    maximum_discount_value = models.DecimalField(max_digits=5, decimal_places=2)
    max_units_per_customer = models.IntegerField()
    single_use = models.BooleanField(default=True)
    needed_item_quantity_to_use = models.IntegerField(default=1)
    applicable_on_item_amount = models.IntegerField()
    id = models.UUIDField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    telephone_number = models.DecimalField(max_digits=10, decimal_places=2)
    verification_code = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name