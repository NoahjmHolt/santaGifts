from django.contrib.auth.models import User
from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse  
from .models import *

# for selenium testing
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
        self.assertContains(response, "<h1>All WishList Items</h1>")
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

    
class giftTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.item = Item.objects.create(title="Test!", price="10")

    def test_model_content(self):
        self.assertEqual(self.item.title, "Test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/items/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("items"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "santa_app/base_template.html")
        self.assertContains(response, "Test!")


# Create your tests here.
class PlayerFormTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Chrome()
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/')
    #find the elements you need to submit form
    item_title = selenium.find_element_by_id('title')
    item_website = selenium.find_element_by_id('website_found')
    item_price = selenium.find_element_by_id('price')
    item_info = selenium.find_element_by_id('about')

    submit = selenium.find_element_by_id('submit_button')

    #populate the form with data
    item_title.send_keys('Basket Ball')
    item_website.send_keys('ballz.net')
    item_price.send_keys('5.99')
    item_info.send_keys('a nice orange one with medium grip and the most anoying ping when bounced!')

    #submit form
    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    assert 'Basket Ball' in selenium.page_source


  def testform2(self):
      selenium = webdriver.Chrome()
      #Choose your url to visit
      selenium.get('http://127.0.0.1:8000/')
      #find the elements you need to submit form
      item_title = selenium.find_element_by_id('title')
      item_website = selenium.find_element_by_id('website_found')
      item_price = selenium.find_element_by_id('price')
      item_info = selenium.find_element_by_id('about')

      submit = selenium.find_element_by_id('submit_button')

      #populate the form with data
      item_title.send_keys('Doggo')
      item_website.send_keys('dogs.bark')
      item_price.send_keys('255.99')
      item_info.send_keys('I want the goodest boy or girl there ever was!')

      #submit form
      submit.send_keys(Keys.RETURN)

      #check result; page source looks at entire html document
      assert 'Doggo' in selenium.page_source

