from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTest(TestCase):
    """ Here we will define the tests that we'll run against our Product model """
    
    def test_str(self):
        test_name = Product(name='A product name')
        self.assertEqual(str(test_name), 'A product name')