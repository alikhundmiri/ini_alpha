from django.contrib import admin
from .models import questions_info

class PostQuestion(admin.ModelAdmin):
    list_display = ["id", "question", "timestamp", "updated"]
    list_filter = ["question", "timestamp", "updated"]
    search_fields = ["question", "detail"]
    class Meta:
        model = questions_info

admin.site.register(questions_info, PostQuestion)
