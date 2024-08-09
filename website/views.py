from django.shortcuts import render
from django.http import HttpResponse


def about_view(request):
    context = {'name': 'Aida Roshani', 'job_title1': 'Software Engineer',
               'job_title2': 'Data Scientist', 'github_link':'https://github.com/Aaidaro',
               'linkedin_link': 'https://www.linkedin.com/in/aida-roshani-73b489181/',}
    
    return render(request, 'website/about.html', context)

def resume_view(request):
    return render(request, 'website/resume.html')

def project_view(request):
    return render(request, 'website/projects.html')

def project_single_view(request):
    context = {'developers_name': 'Aida Roshani',
               "project_link_github":"https://github.com/Aaidaro/Resume",
               "project_link_preview":"github.com/Aaidaro/Resume",
               "date":"27 July, 2022",}
    return render(request, 'website/project_main.html', context)