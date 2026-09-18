from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from facilities.models import Facility
from .models import Assessment, AssessmentAnswer, Question


def risk_from_percentage(percentage):
    if percentage >= 80:
        return "low", "Good SL2 posture. Keep monitoring and reviewing controls."
    if percentage >= 50:
        return "medium", "Some gaps remain. Prioritise segmentation, access control and monitoring."
    return "high", "High risk. Treat network segmentation and remote access as urgent."


@login_required
def assessment_form(request, facility_id):
    facility = get_object_or_404(Facility, pk=facility_id, owner=request.user)
    questions = Question.objects.all().order_by("order")

    if not questions.exists():
        messages.error(request, "No questions have been added yet. Add them in admin.")
        return redirect("facility-list")

    if request.method == "POST":
        score = 0
        max_score = 0
        answers = []
        missing = False

        for question in questions:
            key = f"question_{question.id}"
            value = request.POST.get(key)
            if value not in ("yes", "no"):
                missing = True
                continue
            max_score += question.points
            if value == "yes":
                score += question.points
            answers.append((question, value))

        if missing:
            messages.error(request, "Please answer every question.")
            return render(
                request,
                "assessments/form.html",
                {"facility": facility, "questions": questions},
            )

        percentage = round((score / max_score) * 100) if max_score else 0
        risk_level, recommendation = risk_from_percentage(percentage)

        assessment = Assessment.objects.create(
            facility=facility,
            created_by=request.user,
            score=score,
            max_score=max_score,
            percentage=percentage,
            risk_level=risk_level,
            recommendation=recommendation,
        )
        for question, value in answers:
            AssessmentAnswer.objects.create(
                assessment=assessment,
                question=question,
                answer=value,
            )
        messages.success(request, "Assessment saved.")
        return redirect("assessment-detail", pk=assessment.pk)

    return render(
        request,
        "assessments/form.html",
        {"facility": facility, "questions": questions},
    )


@login_required
def assessment_detail(request, pk):
    assessment = get_object_or_404(
        Assessment,
        pk=pk,
        created_by=request.user,
    )
    return render(
        request,
        "assessments/detail.html",
        {"assessment": assessment},
    )
