from django.test import SimpleTestCase
from django.urls import resolve, reverse
from blog.views import about, setup, int_ngos, Index, AddNGOForm, NGODetails, NGOList
from blog.models import NGO

class TestUrls(SimpleTestCase):

    def test_about_url(self):
        url= reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_setup_url(self):
        url= reverse('setup')
        self.assertEquals(resolve(url).func, setup)
    
    def test_int_ngos_url(self):
        url= reverse('int-ngos')
        self.assertEquals(resolve(url).func, int_ngos)
    
    def test_Index_url(self):
        url= reverse('index')
        self.assertEquals(resolve(url).func.view_class, Index)
    
    def test_AddNGOForm_url(self):
        url= reverse('add_ngo')
        self.assertEquals(resolve(url).func.view_class, AddNGOForm)
    
    
