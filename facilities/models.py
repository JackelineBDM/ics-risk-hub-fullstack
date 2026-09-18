from django.db import models
from django.contrib.auth.models import User


class Facility(models.Model):
    SECTOR_CHOICES = [
        ('energy', 'Energy'),
        ('water', 'Water'),
        ('manufacturing', 'Manufacturing'),
        ('transport', 'Transport'),
        ('other', 'Other'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='facilities')
    name = models.CharField(max_length=120)
    sector = models.CharField(max_length=20, choices=SECTOR_CHOICES, default='other')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name