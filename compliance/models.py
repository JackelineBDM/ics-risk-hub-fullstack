from django.db import models
from facilities.models import Facility


class Control(models.Model):
    title = models.CharField(max_length=250)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class FacilityControl(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='control_status')
    control = models.ForeignKey(Control, on_delete=models.CASCADE)
    is_implemented = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('facility', 'control')

    def __str__(self):
        status = 'done' if self.is_implemented else 'open'
        return f"{self.facility.name} - {self.control.title} ({status})"