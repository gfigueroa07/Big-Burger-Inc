from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.

def fetch_items(request):
    items = Item.objects.all() # similar to SELECT * FROM Items
    Item.objects.
    
    
    
    return render(request, "items.html", {'items': items})