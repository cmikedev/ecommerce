from django.test import TestCase
from .views import checkout


class StoreViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/checkout/')
        self.assertTemplateUsed(response, 'store/checkout.html')
