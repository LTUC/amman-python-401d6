from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.


class HomeTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse("home")
        response=self.client.get(url)
        self.assertEqual(response, 200)
    
    def test_home_page_template(self):
        url = reverse("home")
        response=self.client.get(url)
        self.assertTemplateUsed(response,"home.html")  
