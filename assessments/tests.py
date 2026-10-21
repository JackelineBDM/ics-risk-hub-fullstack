from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from facilities.models import Facility
from .models import Question, Assessment


class AssessmentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("pat", "pat@test.com", "Pass12345!")
        self.facility = Facility.objects.create(
            owner=self.user, name="Test Plant", sector="energy"
        )
        self.q = Question.objects.create(
            text="Is network segmented?", points=10, order=1
        )

    def test_assessment_form_requires_login(self):
        response = self.client.get(reverse("assessment-form", args=[self.facility.pk]))
        self.assertEqual(response.status_code, 302)

    def test_missing_answer_does_not_save(self):
        self.client.login(username="pat", password="Pass12345!")
        response = self.client.post(
            reverse("assessment-form", args=[self.facility.pk]), {}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Assessment.objects.filter(facility=self.facility).exists())

    def test_yes_answer_saves_assessment(self):
        self.client.login(username="pat", password="Pass12345!")
        response = self.client.post(
            reverse("assessment-form", args=[self.facility.pk]),
            {f"question_{self.q.id}": "yes"},
        )
        self.assertEqual(response.status_code, 302)
        assessment = Assessment.objects.get(facility=self.facility)
        self.assertEqual(assessment.score, 10)
        self.assertEqual(assessment.percentage, 100)
        self.assertEqual(assessment.risk_level, "low")
