from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    #image
    developer = models.CharField(max_length=200,null=True)
    Link = models.CharField(max_length=2083, null=True)
    link_preview = models.CharField(max_length=300, null=True)
    Description = models.TextField(default=True)
    #technology
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)

