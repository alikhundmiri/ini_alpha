from django.contrib import admin
from .models import Post

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    list_filter = ["title", "timestamp", "updated"]
    search_fields = ["title", "timestamp", "updated", "detail", "user"]

    class Meta:
        model = Post

admin.site.register(Post, BlogAdmin)
