from django.urls import path
from . import views

urlpatterns = [
    path("facility/<int:facility_id>/", views.assessment_form, name="assessment-form"),
    path("<int:pk>/", views.assessment_detail, name="assessment-detail"),
]
