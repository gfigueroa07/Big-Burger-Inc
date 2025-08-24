from django.shortcuts import render, redirect, HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_item')
    elif request.method == 'GET':
        form = ItemForm()
    items = Item.objects.all()
    return render(request, 'add_item.html', {'form': form, 'items': items})