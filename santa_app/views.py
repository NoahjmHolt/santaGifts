from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
# Create your views here.
def index(request):

# Render index.html
    return render( request, 'santa_app/index.html')

class ItemListView(generic.ListView):
      model = Item
class ItemDetailView(generic.DetailView):
      model = Item

