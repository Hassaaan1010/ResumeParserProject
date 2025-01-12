from django.urls import path
from .views import extract_resume

urlpatterns = [
    path('extract-resume/', extract_resume, name='extract_resume'),
]
