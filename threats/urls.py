from django.urls import path
from . import views

urlpatterns = [
    path("", views.threat_list, name="threat-list"),
]
