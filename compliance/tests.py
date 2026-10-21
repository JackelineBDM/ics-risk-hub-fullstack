from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from facilities.models import Facility
from .models import Control, FacilityControl


class ChecklistTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("pat", "pat@test.com", "Pass12345!")
        self.facility = Facility.objects.create(owner=self.user, name="Test Plant", sector="energy")
        self.control = Control.objects.create(title="Segment networks", order=1)

    def test_checklist_requires_login(self):
        response = self.client.get(reverse("compliance-checklist", args=[self.facility.pk]))
        self.assertEqual(response.status_code, 302)

    def test_tick_is_saved(self):
        self.client.login(username="pat", password="Pass12345!")
        response = self.client.post(
            reverse("compliance-checklist", args=[self.facility.pk]),
            {"control": [str(self.control.id)]},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            FacilityControl.objects.filter(
                facility=self.facility,
                control=self.control,
                is_implemented=True,
            ).exists()
        )
