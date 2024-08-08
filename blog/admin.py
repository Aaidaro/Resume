from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "published_date"
    list_display = ["id", "title", "published_date", "created_date", "status"]
admin.site.register(Post,PostAdmin)