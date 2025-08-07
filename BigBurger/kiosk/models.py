from django.db import models
from .category import Category

class Customer(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    telephone_number = models.DecimalField(max_digits=10)
    verification_code = models.DecimalField(max_digits=4)

    def __str__(self):
        return self.name
