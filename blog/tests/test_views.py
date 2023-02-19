from django.test import TestCase, Client
from django.urls import reverse
from blog.views import Index
from blog.models import NGO

class TestViews(TestCase):

    def test_Index(self):
        client = Client()

        response = client.get(reverse('ngos'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')