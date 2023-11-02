from django.urls import path
from . import views

urlpatterns = [
    #path function defines a url pattern
    #'' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name='index' parameter is to dynamically create url
    # example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),

    path('items/', views.ItemListView.as_view(), name= 'items'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-details'),

    #forms
    #path('item/<int:item_id>/create_item/', views.CreateItem, name='create_item'),
    path('create_item/', views.CreateItem, name='create_item'),

]
