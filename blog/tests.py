from django.test import TestCase, Client
from django.urls import reverse


class TestStatusCode(TestCase):
    client = Client()

    def test_response_post_list_view(self):
        response = self.client.get(reverse('post_list_view'))
        self.assertEqual(response.status_code, 200)
