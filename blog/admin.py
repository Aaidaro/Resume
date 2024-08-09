from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "published_date"
    list_display = ["title", "created_date", "id", "status", "published_date"]
admin.site.register(Post, PostAdmin)