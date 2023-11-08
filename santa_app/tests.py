from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse  
from .models import *


class HomepageTests(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "santa_app/index.html")

    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "<h1>Personal WishList Items</h1>")
        self.assertNotContains(response, "Not on the page")


class ListPageTests(TestCase):  # new helped: https://stackoverflow.com/questions/57007022/assertion-error-while-testing-django-views
    def test_url_exists_at_correct_location(self): 
        response = self.client.get("/items/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("items"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("items"))
        self.assertTemplateUsed(response, "santa_app/item_list.html")

    def test_template_content(self):
        response = self.client.get(reverse("items"))
        self.assertContains(response, "<h1>Wish List</h1>")
        self.assertNotContains(response, "Should not be here!")

