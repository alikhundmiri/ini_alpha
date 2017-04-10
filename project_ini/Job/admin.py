from django.contrib import admin
from .models import job_database


class jobAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    list_filter = ["title", "timestamp", "updated"]
    search_fields = ["title", "timestamp", "updated", "detail", "user"]

    class Meta:
        model = job_database


admin.site.register(job_database, jobAdmin)
