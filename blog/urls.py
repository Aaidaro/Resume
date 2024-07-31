from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_main_view, name= "main"),
    path('single/', single_blog_view, name= "single"),
]