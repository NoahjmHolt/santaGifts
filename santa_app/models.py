from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
        title = models.CharField(max_length=200)
        website_found = models.CharField(max_length=200, blank=True)
        price = models.CharField(max_length=10)
        about = models.TextField(blank=True)

        def __str__(self):
            return self.title

        def get_absolute_url(self):
            return reverse('item-details', args=[str(self.id)])
  
