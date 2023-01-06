from django.test import TestCase
from .views import cart


class StoreViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/cart/')
        self.assertTemplateUsed(response, 'store/cart.html')
