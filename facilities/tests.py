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
        own = Facility.objects.create(
            owner=self.user, name="North Plant Alpha", sector="energy"
        )
        Facility.objects.create(
            owner=self.other, name="South Plant Beta", sector="energy"
        )
        self.client.login(username="pat", password="Pass12345!")
        response = self.client.get(reverse("facility-list"))
        self.assertContains(response, "North Plant Alpha")
        self.assertNotContains(response, "South Plant Beta")
        self.assertEqual(list(response.context["facilities"]), [own])

    def test_create_facility(self):
        self.client.login(username="pat", password="Pass12345!")
        response = self.client.post(reverse("facility-add"), {
            "name": "New Test Plant",
            "sector": "energy",
            "description": "test",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Facility.objects.filter(name="New Test Plant", owner=self.user).exists())

    def test_other_user_cannot_edit(self):
        facility = Facility.objects.create(owner=self.other, name="Other Plant", sector="energy")
        self.client.login(username="pat", password="Pass12345!")
        response = self.client.get(reverse("facility-edit", args=[facility.pk]))
        self.assertEqual(response.status_code, 404)
