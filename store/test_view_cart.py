from django.test import TestCase
from django.urls import reverse
from .views import cart


class StoreViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
