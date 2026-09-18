from django.shortcuts import render
from .models import Threat


def threat_list(request):
    threats = Threat.objects.all()
    impact = request.GET.get("impact")
    if impact in ("medium", "high", "critical"):
        threats = threats.filter(impact=impact)
    return render(
        request,
        "threats/list.html",
        {"threats": threats, "selected_impact": impact or ""},
    )
