from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import *

# Create your views here.
def index(request):

# Render index.html
    return render( request, 'santa_app/index.html')

class ItemListView(generic.ListView):
      model = Item
class ItemDetailView(generic.DetailView):
      model = Item

def CreateItem(request):
     
     item_form = ItemForm()

     if request.method == 'POST':
          item_form = ItemForm(request.POST)
          if item_form.is_valid():
               item_form.save()
               return redirect('/items')

     context = {'item_form':item_form}
     
     return render(request, 'santa_app/item_form.html', context)

def UpdateItem(request, pk):
     
     item = Item.objects.get(id=pk)
     item_form = ItemForm(instance=item)

     if request.method == 'POST':
          item_form = ItemForm(request.POST, instance=item)
          if item_form.is_valid():
               item_form.save()
               return redirect('/items')
          
     context = {'item_form':item_form}

     return render(request, 'santa_app/item_form.html', context)
