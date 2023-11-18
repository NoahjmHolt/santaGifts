from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render( request, 'santa_app/index.html')

class ItemListView(generic.ListView):
      model = Item
class ItemDetailView(generic.DetailView):
      model = Item
      

def RegisterPage(request):

     if request.user.is_authenticated:
          return redirect('items')
     else:
          form = CreateUserForm()

          if request.method == 'POST':
               form = CreateUserForm(request.POST)
               if form.is_valid():
                    form.save()
                    messages.success(request, 'Account creation successful!')
                    return redirect('login')


     context = {'form':form}
     return render(request, 'santa_app/register.html', context)


def LoginPage(request):

     if request.user.is_authenticated:
          return redirect('items')
     else:
          if request.method == 'POST':
               username = request.POST.get('username')
               password = request.POST.get('password')

               user = authenticate(request, username=username, password=password)

               if user is not None:
                    login(request, user)
                    return redirect('items')
               else:
                    messages.info(request, 'Username OR Password is incorrect')

     context = {}
     return render(request, 'santa_app/login.html', context)


def LogoutUser(request):
     logout(request)
     return redirect('login')


@login_required(login_url='login')
def CreateItem(request):
     
     item_form = ItemForm()

     if request.method == 'POST':
          item_form = ItemForm(request.POST)
          if item_form.is_valid():
               item_form.save()
               return redirect('/items')

     context = {'item_form':item_form}
     
     return render(request, 'santa_app/item_form.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def DeleteItem(request, pk):
     
     item = Item.objects.get(id=pk)

     if request.method == 'POST':
          item.delete()
          return redirect('/items')

     context = {'item':item}
     return render(request, 'santa_app/delete.html', context)
