from django.urls import path
from website.views import *

urlpatterns = [
    path('', about_view),
    path('resume', resume_view),
    path('projects', project_view)
]
