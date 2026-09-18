from django.db import models
from django.contrib.auth.models import User
from facilities.models import Facility


class Question(models.Model):
    text = models.CharField(max_length=300)
    points = models.PositiveIntegerField(default=10)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.text}"


class Assessment(models.Model):
    RISK_CHOICES = [
        ('low', 'Low Risk'),
        ('medium', 'Medium Risk'),
        ('high', 'High Risk'),
    ]

    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='assessments')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    max_score = models.PositiveIntegerField(default=0)
    percentage = models.PositiveIntegerField(default=0)
    risk_level = models.CharField(max_length=10, choices=RISK_CHOICES, default='high')
    recommendation = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.facility.name} - {self.percentage}%"


class AssessmentAnswer(models.Model):
    ANSWER_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=3, choices=ANSWER_CHOICES)

    class Meta:
        unique_together = ('assessment', 'question')

    def __str__(self):
        return f"{self.question.order}: {self.answer}"