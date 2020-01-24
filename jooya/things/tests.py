from django.test import TestCase
from django.core.urlresolvers import reverse


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)