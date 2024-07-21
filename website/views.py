from django.shortcuts import render
from django.http import HttpResponse

def about_view(request):
    return HttpResponse('<h1>About</h1>')

def resume_view(request):
    return HttpResponse('<h1>Resume</h1>')

def project_view(request):
    return HttpResponse('<h1>Project</h1>')