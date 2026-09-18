from django.db import models


class Threat(models.Model):
    IMPACT_CHOICES = [
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    name = models.CharField(max_length=120)
    description = models.TextField()
    purdue_level = models.CharField(max_length=20)
    impact = models.CharField(max_length=10, choices=IMPACT_CHOICES, default='high')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name