from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from facilities.models import Facility
from .models import Control, FacilityControl


@login_required
def checklist(request, facility_id):
    facility = get_object_or_404(Facility, pk=facility_id, owner=request.user)
    controls = Control.objects.all().order_by("order")

    if request.method == "POST":
        checked_ids = set(request.POST.getlist("control"))
        for control in controls:
            obj, _created = FacilityControl.objects.get_or_create(
                facility=facility,
                control=control,
            )
            obj.is_implemented = str(control.id) in checked_ids
            obj.save()
        messages.success(request, "Checklist saved.")
        return redirect("compliance-checklist", facility_id=facility.id)

    status = {
        item.control_id: item.is_implemented
        for item in FacilityControl.objects.filter(facility=facility)
    }
    rows = [
        {"control": control, "is_implemented": status.get(control.id, False)}
        for control in controls
    ]
    done = sum(1 for row in rows if row["is_implemented"])
    total = len(rows)
    percent = round((done / total) * 100) if total else 0
    return render(
        request,
        "compliance/checklist.html",
        {
            "facility": facility,
            "rows": rows,
            "done": done,
            "total": total,
            "percent": percent,
        },
    )
