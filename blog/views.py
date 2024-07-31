from django.shortcuts import render

def blog_main_view(request):
    return render(request, 'blog/blog_main.html')

def single_blog_view(request):
    return render(request, 'blog/blog_single.html')