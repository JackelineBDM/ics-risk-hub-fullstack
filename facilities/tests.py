from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Facility


class FacilityTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("pat", "pat@test.com", "Pass12345!")
        self.other = User.objects.create_user("sam", "sam@test.com", "Pass12345!")

    def test_login_required_for_list(self):
        response = self.client.get(reverse("facility-list"))
        self.assertEqual(response.status_code, 302)

    def test_user_only_sees_own_facility(self):
        Facility.objects.create(owner=self.user, name="A", sector="energy")
        Facility.objects.create(owner=self.other, name="B", sector="energy")
        self.client.login(username="pat", password="Pass12345!")
        response = self.client.get(reverse("facility-list"))
        self.assertContains(response, "A")
        self.assertNotContains(response, "B")
