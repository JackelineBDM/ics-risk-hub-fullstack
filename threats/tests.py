from django.test import TestCase
from django.urls import reverse


class ThreatTests(TestCase):
    def test_threat_list_ok(self):
        response = self.client.get(reverse("threat-list"))
        self.assertEqual(response.status_code, 200)
