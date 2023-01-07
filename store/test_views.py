from django.test import TestCase
from . import views


class PageViewTest(TestCase):

    def test_store_page_loads_correctly(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/store.html')

    def test_cart_page_loads_correctly(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/cart.html')

    def test_checkout_page_loads_correctly(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/checkout.html')