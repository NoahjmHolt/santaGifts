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
    path('create_item/', views.CreateItem, name='create_item'),
    path('update_item/<int:pk>', views.UpdateItem, name='update_item'),
    path('delete_item/<int:pk>', views.DeleteItem, name='delete_item'),

    #login/reg/logout
    path('register/', views.RegisterPage, name='register'),
    path('login/', views.LoginPage, name='login'),

]
