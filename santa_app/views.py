from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render( request, 'santa_app/index.html')

class ItemListView(generic.ListView):
      model = Item
class ItemDetailView(generic.DetailView):
      model = Item

def RegisterPage(request):
     form = UserCreationForm()
     context = {'form'}
     return render(request, 'santa_app/register.html', context)

def LoginPage(request):
     context = {}
     return render(request, 'santa_app/login.html', context)

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


def DeleteItem(request, pk):
     
     item = Item.objects.get(id=pk)

     if request.method == 'POST':
          item.delete()
          return redirect('/items')

     context = {'item':item}
     return render(request, 'santa_app/delete.html', context)
