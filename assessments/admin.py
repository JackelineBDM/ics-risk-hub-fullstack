from django.contrib import admin
from .models import Question, Assessment, AssessmentAnswer

admin.site.register(Question)
admin.site.register(Assessment)
admin.site.register(AssessmentAnswer)