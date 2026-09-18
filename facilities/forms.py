from django import forms
from .models import Facility


class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ["name", "sector", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "sector": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
