from django.db import models

class Customer(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    telephone_number = models.DecimalField(max_digits=10)
    verification_code = models.DecimalField(max_digits=4)

    def __str__(self):
        return self.name

class Items(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True)
    name = models.CharField(unique=True)
    category = models.CharField(unique=True, max_length=20)
    picture = models.ImageField(upload_to='item_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)
    
class Coupons(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True)
    items_id = models.ForeignKey(Items, auto_created=True)
    name = models.CharField(unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    discount_percentage = models.IntegerField(max_lenght=2) 
    maximum_discount_value = models.DecimalField(max_digits=5, decimal_places=2)
    max_units_per_customer = models.IntegerField(max_length=1)
    single_use = models.BooleanField(default=True)
    needed_item_quantity_to_use = models.IntegerField(default=1)
    applicable_on_item_amount = models.IntegerField(max_length=1)
    