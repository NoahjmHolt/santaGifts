from django.forms import ModelForm
from .models import *

# for the login and register classes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create class for project form
class ItemForm(ModelForm):

    class Meta:
        model = Item
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','email', 'password1', 'password2']