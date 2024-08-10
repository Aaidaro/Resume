from django.shortcuts import render
from django.http import HttpResponse


def about_view(request):
    return render(request, 'website/about.html')

def resume_view(request):
    return render(request, 'website/resume.html')

def project_view(request):
    return render(request, 'website/projects.html')

def project_single_view(request):
    context = {'developer': 'Aida Roshani',
               "project_link_github":"https://github.com/Aaidaro/Resume",
               "link_preview":"github.com/Aaidaro/Resume",
               "date":"27 July, 2022",}
    return render(request, 'website/project_main.html', context)