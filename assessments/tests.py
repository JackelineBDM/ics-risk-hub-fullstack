from django.test import TestCase
from django.urls import reverse


class AssessmentTests(TestCase):
    def test_assessment_form_requires_login(self):
        response = self.client.get(reverse("assessment-form", args=[1]))
        self.assertEqual(response.status_code, 302)
