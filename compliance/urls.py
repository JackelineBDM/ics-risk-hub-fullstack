from django.urls import path
from . import views

urlpatterns = [
    path("facility/<int:facility_id>/", views.checklist, name="compliance-checklist"),
]
