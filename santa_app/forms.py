from django.forms import ModelForm
from .models import *

#create class for project form
class ItemForm(ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
