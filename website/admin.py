from django.contrib import admin
from website.models import Project

class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["title", "developer", "Link", "created_date"]
admin.site.register(Project,ProjectAdmin)