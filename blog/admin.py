from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "published_date"
    list_display = ["title", "created_date","author", "id", "status", "published_date"]
    list_filter = ["author", "status"]
admin.site.register(Post, PostAdmin)