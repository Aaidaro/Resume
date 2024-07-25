from django.urls import path
from website.views import *

urlpatterns = [
    path('', about_view, name= "about"),
    path('resume/', resume_view, name= "resume"),
    path('projects/', project_view, name= "projects")
]
