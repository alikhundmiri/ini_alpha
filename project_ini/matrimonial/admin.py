from django.contrib import admin
from .models import mat_info


class PostMat(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    list_filter = ["title", "timestamp", "updated"]
    search_fields = ["description","title",]

    class Meta:
        model = mat_info


admin.site.register(mat_info, PostMat)
