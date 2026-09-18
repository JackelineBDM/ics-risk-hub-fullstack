from django.urls import path
from .views import (
    FacilityListView,
    FacilityCreateView,
    FacilityUpdateView,
    FacilityDeleteView,
)

urlpatterns = [
    path("", FacilityListView.as_view(), name="facility-list"),
    path("add/", FacilityCreateView.as_view(), name="facility-add"),
    path("<int:pk>/edit/", FacilityUpdateView.as_view(), name="facility-edit"),
    path("<int:pk>/delete/", FacilityDeleteView.as_view(), name="facility-delete"),
]
